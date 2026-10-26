"""Check STL edge closure and create a technical preview from the actual meshes."""
from pathlib import Path
from collections import Counter
import json
import struct
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

root=Path(__file__).parent
fig=plt.figure(figsize=(15,13),facecolor='#f4f6f8')
checks={}
names=['body','front_bezel','rear_cover','mount_fit_check','power_slider','power_slider_cap','button_extension','control_fit_check']
for i,name in enumerate(names):
    data=(root/f'{name}.stl').read_bytes()
    n=struct.unpack_from('<I',data,80)[0]
    records=np.frombuffer(data,dtype=np.dtype([('normal','<f4',3),('v','<f4',(3,3)),('attr','<u2')]),offset=84,count=n)
    triangles=records['v'].astype(float)
    edges=Counter()
    directed=Counter()
    for tri in triangles:
        verts=[tuple(np.round(v,5)) for v in tri]
        for a,b in zip(verts,verts[1:]+verts[:1]):
            edges[tuple(sorted((a,b)))]+=1
            directed[(a,b)]+=1
    bad=sum(v!=2 for v in edges.values())
    orientation=sum(v!=directed.get((b,a),0) for (a,b),v in directed.items())
    volume=float(np.einsum('ij,ij->i',triangles[:,0],np.cross(triangles[:,1],triangles[:,2])).sum()/6)
    assert bad==0,(name,'open/nonmanifold edges',bad)
    assert orientation==0,(name,'inconsistent winding')
    assert volume>0,(name,'nonpositive signed volume')
    checks[name]={'triangles':n,'open_or_nonmanifold_edges':bad,'winding_errors':orientation,'signed_volume_mm3':round(volume,2)}
    ax=fig.add_subplot(3,3,i+1,projection='3d',facecolor='#f4f6f8')
    from matplotlib.colors import to_rgb
    normals=np.cross(triangles[:,1]-triangles[:,0],triangles[:,2]-triangles[:,0])
    normals/=np.maximum(np.linalg.norm(normals,axis=1)[:,None],1e-12)
    light=np.array([-0.3,-0.5,0.8]); light/=np.linalg.norm(light)
    brightness=0.45+0.55*np.maximum(normals@light,0)
    colors=brightness[:,None]*np.array(to_rgb(['#7f9baa','#abb9bf','#93a7ac','#d6a75e','#d6a75e','#e6bb7a','#d6a75e','#7f9baa'][i]))
    mesh=Poly3DCollection(triangles,facecolor=colors,edgecolor='none',alpha=1)
    ax.add_collection3d(mesh)
    low=triangles.min(axis=(0,1)); high=triangles.max(axis=(0,1))
    ax.set_xlim(low[0]-2,high[0]+2); ax.set_ylim(low[1]-2,high[1]+2); ax.set_zlim(0,max(15,high[2]+2))
    ax.set_box_aspect((max(5,high[0]-low[0]+4),max(5,high[1]-low[1]+4),max(5,high[2]+2)))
    ax.view_init(58,-65)
    ax.set_title(name.replace('_',' ').title(),fontsize=15)
    ax.set_axis_off()
fig.suptitle('Arc reactor housing — revision 5\nReinforced two-hole lanyard lug · guided controls · 15 mm finger well',fontsize=19)
fig.tight_layout(rect=[0,0,1,0.93])
fig.savefig(root/'preview.png',dpi=160)
(root/'mesh_validation.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
