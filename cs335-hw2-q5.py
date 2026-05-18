#CPSC 335
#Group 4
#HW2 Q5

def min_cost_exact_masks(pack_options, num_masks):
    """
    Finds the minimum cost to purchase exactly 'n' masks.
    
    pack_options: A list of tuples, where each tuple is (masks_in_pack, cost)
    n: The exact total number of masks required
    return: A list of the chosen packs to achieve the minimum cost, or an error message
    """
    
    # 1. Initialize DP and pack_used arrays
    # DP array stores the minimum cost for 'j' masks. Initialized to infinity.
    DP = [float('inf')] * (num_masks + 1)   #0...n = (n+1)
    
    # pack_used array stores the index of the pack used to reach that minimum cost.
    pack_used = [-1] * (num_masks + 1)
    
    # Base case: 0 cost for 0 masks
    DP[0] = 0
    
    # 2 & 3. Fill the DP table using the recurrence rule
    for j in range(1, num_masks + 1):   # 1...num_masks_needed
        for i in range(len(pack_options)):     #0...num_pack_options
            k_i = pack_options[i][0]  # Number of masks in pack i
            c_i = pack_options[i][1]  # Cost of pack i
            
            # If the pack size is smaller than or equal to current target masks
            if k_i <= j:
                # If using this pack yields a smaller cost than what we have
                if DP[j - k_i] + c_i < DP[j]:
                    DP[j] = DP[j - k_i] + c_i
                    pack_used[j] = i  # Remember the index of the chosen pack

    # 4. Reconstruct the list of chosen packs
    # If the target n still has a cost of infinity, it's impossible to reach
    if DP[num_masks] == float('inf'):
        return f"No valid combination to buy exactly {num_masks} masks."
        
    chosen_packs = []
    current = num_masks
    
    # Trace backward from n down to 0
    while current > 0:
        best_pack_index = pack_used[current]
        chosen_packs.append(pack_options[best_pack_index])
        
        # Subtract the amount of masks in the chosen pack to trace backward
        current -= pack_options[best_pack_index][0]
        
    return chosen_packs


# ==========================================
# Example Usage (Based on our walkthrough)
# ==========================================

def main():
    # Available packs: (quantity, cost)
    # Pack 1: 2 masks for $3
    # Pack 2: 3 masks for $4
    mask_pack_options = [(2, 3), (3, 4)]
    masks_needed = 6
    
    best_purchases = min_cost_exact_masks(mask_pack_options, masks_needed)
    
    print(f"Masks Needed: {masks_needed}")
    print(f"Packs to buy: {best_purchases}")

if __name__ == "__main__":
    main()