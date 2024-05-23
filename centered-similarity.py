import numpy as np

rx = np.array([-2.6, 0, -0.6, 0, 0, 1.4, 0, 0, 1.4, 0, 0.4, 0])
ry = np.array([0,0,1.84,0.84,0,0,0.84,0,0,-1.16,-2.16,-0.16])

rx_mean = np.mean(rx)
ry_mean = np.mean(ry)

rx_centered = rx - rx_mean
ry_centered = ry - ry_mean

dot_product = np.dot(rx_centered, ry_centered)
rx_centered_norm = np.linalg.norm(rx_centered)
ry_centered_norm = np.linalg.norm(ry_centered)

centered_cos_theta = dot_product / (rx_centered_norm * ry_centered_norm)

print(centered_cos_theta)
