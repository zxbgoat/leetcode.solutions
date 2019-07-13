import sys

def median(nums1, nums2):
    i, j = len(nums1) // 2, len(nums2) // 2
    if nums1[i] <= nums2[j+1] and nums2[j] <= nums1[i+1]:
        return nums1[i], nums2[j]
    elif nums1[i] > nums2[j+1]:
        return median(nums1[])
