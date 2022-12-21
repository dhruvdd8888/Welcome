def findMedianSortedArrays(nums1,nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l=len(nums1)
        if(l&1):return nums1[int((l-1)/2)]
        return (nums1[int(l/2-1)]+nums1[int(l/2)])/2