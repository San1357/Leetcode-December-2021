

# Time complexity: O(N)
# Space complexity: O(1)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        
        pivot = self.choose_pivot(points, left, right)
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
    def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        
        return points[left + (right - left) // 2]
    
    def squared_distance(self, point: List[int]) -> int:
        
        return point[0] ** 2 + point[1] ** 2
