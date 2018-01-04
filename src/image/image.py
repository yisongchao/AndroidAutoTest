#!/usr/bin/env python
# -*- coding: utf-8 -*-



#import numpy as np
import cv2
#from matplotlib import pyplot as plt


MIN_MATCH_COUNT = 1

def _middlePoint(pts):
    def add(p1, p2):
        return (p1[0]+p2[0], p1[1]+p2[1])
    def distance(p1, p2):
        import math
        l2 = (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])
        return math.sqrt(l2)
    # debug
    for p in pts:
        print 'Point:', p.pt
    length = len(pts)
    print length
    sumx, sumy = reduce(add, [p.pt for p in pts])
    point = sumx/length, sumy/length
    print 'step1: result=', point

    # filter out ok points
    avg_distance = sum([distance(point, p.pt) for p in pts])/length
    print 'avg distance=', avg_distance
    good = []
    sumx, sumy = 0.0, 0.0
    for p in pts:
        print 'point: %s, distance: %.2f' %(p.pt, distance(p.pt, point))
        if distance(p.pt, point) <= 1*avg_distance:
            good.append(p.pt)
            sumx += p.pt[0]
            sumy += p.pt[1]
        else:
            print 'not good', p.pt
    print 'step1: result=', point
    point = map(int, (sumx/len(good), sumy/len(good)))
    print 'step2: point=', point
    return point

def find_image_position(origin='origin.png', query='query.png', outfile=None):
    '''
    find all image positions
    @return None if not found else a tuple: (origin.shape, query.shape, postions)
    might raise Exception
    '''
    img1 = cv2.imread(query, 0) # query image(small)
    img2 = cv2.imread(origin, 0) # train image(big)
    img_tmp = cv2.imread(outfile, 0)
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    #print len(des1), len(des2)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    # flann


    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
    print len(kp1), len(kp2), 'good cnt:', len(good)

    #if len(good)*1.0/len(kp1) < 0.5:
    if len(good)<MIN_MATCH_COUNT:
        print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
        return img2.shape, img1.shape, []

    queryPts = []
    trainPts = []
    for dm in good:
        queryPts.append(kp1[dm.queryIdx])
        trainPts.append(kp2[dm.trainIdx])

    img3 = cv2.drawKeypoints(img1, queryPts, img_tmp)
    cv2.imwrite(outfile, img3)

    img3 = cv2.drawKeypoints(img2, trainPts, img_tmp)
    print trainPts
    point = _middlePoint(trainPts)
    print 'position in', point

    if outfile:
        edge = 10
        top_left = (point[0]-edge, point[1]-edge)
        bottom_right = (point[0]+edge, point[1]+edge)
        cv2.rectangle(img3, top_left, bottom_right, 255, 2)
        cv2.imwrite(outfile, img3)
    return img2.shape, img1.shape, [point]

if __name__ == '__main__':
    pts = find_image_position('image_repo/login_qq_1509208753.png', 'image_repo/login_qq.png',
        outfile='image_repo/result.png')
    print pts