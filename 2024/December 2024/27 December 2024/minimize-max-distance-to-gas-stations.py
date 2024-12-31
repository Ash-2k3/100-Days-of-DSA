class Solution:
    def minimiseMaxDistance(self, arr, k):
        gasStationsPlaced = 0
        gasStationsPos = arr.copy()

        while gasStationsPlaced < k:
            # Step 1: Generate adjacent distance array
            adjacentDistArr = self.generateAdjacentDistance(gasStationsPos)
            
            # Step 2: Place gas station in the segment with maximum distance
            gasStationsPos = self.placeGasStation(gasStationsPos, adjacentDistArr)
            
            gasStationsPlaced += 1
        
        # Calculate the maximum distance after placing all gas stations
        final_max_distance = max(
            gasStationsPos[i + 1] - gasStationsPos[i]
            for i in range(len(gasStationsPos) - 1)
        )
        return round(final_max_distance, 6)

    def generateAdjacentDistance(self, arr):
        # Calculate distances between adjacent gas stations
        adjacent_distances = []
        for i in range(1, len(arr)):
            adjacent_distances.append(arr[i] - arr[i - 1])
        return adjacent_distances

    def placeGasStation(self, pos_arr, adjacent_dist_arr):
        # Find the largest gap
        max_distance = max(adjacent_dist_arr)
        max_distance_index = adjacent_dist_arr.index(max_distance)
        
        # Calculate the new gas station position (midpoint of the largest gap)
        new_pos = (pos_arr[max_distance_index] + pos_arr[max_distance_index + 1]) / 2
        
        # Insert the new gas station into the correct position
        pos_arr.insert(max_distance_index + 1, new_pos)
        
        return pos_arr
