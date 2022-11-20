import numpy as np
np.set_printoptions(suppress=True) 
# 作用是取消numpy默认的科学计数法，测试表明open3d点云读取函数没法读取科学计数法的表示
import open3d as o3d
data = np.load('./modelnet/bathtub/test/bathtub_0109.npy')
print(data)
txt_data = np.savetxt('scene1.txt', data)
#pcd = o3d.io.read_point_cloud('scene1.txt', format='xyzrgb')
pcd = o3d.io.read_point_cloud('scene1.txt', format='xyz')
# 此处因为npy里面正好是 x y z r g b的数据排列形式，所以format='xyzrgb'
print(pcd)
o3d.visualization.draw_geometries([pcd], width=1200, height=600) # 可视化点云
