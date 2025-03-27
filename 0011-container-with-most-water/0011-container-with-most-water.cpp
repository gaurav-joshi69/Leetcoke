class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0,right=height.size()-1;
        int maxwater=0;
        int water=0;
        while(left<right){
            if(height[left]<=height[right]){
                water=(right-left)*min(height[left],height[right]);
                left+=1;
            }
            else{
                 water=(right-left)*min(height[left],height[right]);
                right-=1;
            }
            maxwater=max(maxwater,water);
        }
        return maxwater;
    }
};