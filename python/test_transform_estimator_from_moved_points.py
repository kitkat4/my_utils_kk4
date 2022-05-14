#!/usr/bin/env python3

from my_utils_kk4 import TransformEstimatorFromMovedPoints
from scipy.spatial.transform import Rotation
import numpy as np
import sys

if __name__ == '__main__':

    estimator = TransformEstimatorFromMovedPoints()

    sample_size = 20

    euler_gt = [20, 10, 30]

    rot_gt = Rotation.from_euler('zyx', euler_gt, degrees=True).as_matrix()
    tl_gt = np.array([0.5, 2.0, -1.0]).reshape((3, 1))
    
    org_samples = np.random.rand(3, sample_size)
    moved_samples = np.dot(rot_gt, org_samples) + tl_gt

    estimator.set_samples(org_samples, moved_samples)

    (tl_estimated, rot_estimated) = estimator.estimate(is_alibi=True)

    sys.stdout.write(
        '==== RESULT ====\n' +
        '<Translation>\n' +
        'Ground truth: \n' +
        str(tl_gt) + '\n' +
        'Estimated: \n' +
        str(tl_estimated) + '\n' +
        '<Rotation>\n' +
        'Ground truth: \n' +
        str(rot_gt) + '\n' +
        'Estimated:\n' +
        str(rot_estimated) + '\n' +
        'Input original samples:\n' +
        str(org_samples.T) + '\n' +
        'Input moved samples:\n' +
        str(moved_samples.T) + '\n')



