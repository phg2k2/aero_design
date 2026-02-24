from stl import mesh

# Đọc file STL
your_mesh = mesh.Mesh.from_file('vtol_m.stl')

# Trích xuất các thông số kỹ thuật
print(f"Số lượng tam giác: {len(your_mesh.vectors)}")
print(f"Pháp tuyến của tam giác đầu tiên: {your_mesh.normals[0]}")
print(f"Tọa độ 3 đỉnh của tam giác đầu tiên:\n{your_mesh.vectors[0]}")

# Tính toán các đặc tính vật lý cơ bản
volume, cog, inertia = your_mesh.get_mass_properties()
print(f"Thể tích: {volume}")
print(f"Trọng tâm (CoG): {cog}")