import numpy as np
import argparse
import open3d as o3d
import os
import sys
import termios

def press_any_key_exit():
  # 获取标准输入的描述符
  fd = sys.stdin.fileno()
  # 获取标准输入(终端)的设置
  old_ttyinfo = termios.tcgetattr(fd)
  # 配置终端
  new_ttyinfo = old_ttyinfo[:]
  # 使用非规范模式(索引3是c_lflag 也就是本地模式)
  new_ttyinfo[3] &= ~termios.ICANON
  # 关闭回显(输入不会被显示)
  new_ttyinfo[3] &= ~termios.ECHO
  # 输出信息
  #sys.stdout.write(msg)
  #sys.stdout.flush()
  # 使设置生效
  termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
  # 从终端读取
  os.read(fd, 7)
  # 还原终端设置
  termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

if __name__=="__main__":
  parse = argparse.ArgumentParser(description="point cloud visualization")
  parse.add_argument('--path', type=str, default='./', help='root path')
  parse.add_argument('--file', type=str, help='root path')
  parse.add_argument('--normal', type=bool, default=False,help='root path')
  args = parse.parse_args()
  np.set_printoptions(suppress=True) 
  # 作用是取消numpy默认的科学计数法，测试表明open3d点云读取函数没法读取科学计数法的表示
  if args.file :
    #press_any_key_exit()
    data = np.load(args.file)
    print(data)
    print(type(data))
    txt_data = np.savetxt('scene1.txt', data)
    #pcd = o3d.io.read_point_cloud('scene1.txt', format='xyzrgb')
    pcd = o3d.io.read_point_cloud('scene1.txt', format='xyz')
    # 此处因为npy里面正好是 x y z r g b的数据排列形式，所以format='xyzrgb'
    print(pcd)
    print(type(pcd))
    if args.normal:
      pcd.voxel_down_sample(voxel_size=0.0564)
      pcd.estimate_normals(search_param = o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    o3d.visualization.draw_geometries([pcd], window_name="Point 3D",width=1200, height=600, point_show_normal=True) # 可视化点云
    #o3d.visualization.draw([pcd],width=1200, height=600) # 可视化点云
    #o3d.visualization.draw_geometries([pcd], width=1200, height=600, point_show_normal=True, mesh_show_wireframe=True, mesh_show_back_face=True) # 可视化点云
    #o3d.visualization.draw_geometries([pcd], width=1200, height=600, point_show_normal=True, mesh_show_wireframe=True, mesh_show_back_face=True) # 可视化点云
  else:
    print("inpur file and path")
  if args.path:
    filelist = os.listdir(args.path)
    for i in filelist:
      print(i)
      press_any_key_exit()
      data = np.load(os.path.join(args.path,i))
      print(data)
      print(type(data))
      txt_data = np.savetxt('scene1.txt', data)
      #pcd = o3d.io.read_point_cloud('scene1.txt', format='xyzrgb')
      pcd = o3d.io.read_point_cloud('scene1.txt', format='xyz')
      # 此处因为npy里面正好是 x y z r g b的数据排列形式，所以format='xyzrgb'
      print(pcd)
      print(type(pcd))
      if args.normal:
        pcd.voxel_down_sample(voxel_size=0.0564)
        pcd.estimate_normals(search_param = o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
      o3d.visualization.draw_geometries([pcd], window_name="Point 3D",width=1200, height=600, point_show_normal=True) # 可视化点云
      #o3d.visualization.draw([pcd],width=1200, height=600) # 可视化点云
      #o3d.visualization.draw_geometries([pcd], width=1200, height=600, point_show_normal=True, mesh_show_wireframe=True, mesh_show_back_face=True) # 可视化点云
      #o3d.visualization.draw_geometries([pcd], width=1200, height=600, point_show_normal=True, mesh_show_wireframe=True, mesh_show_back_face=True) # 可视化点云
  else:
    print("inpur file and path")
