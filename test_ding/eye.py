import os
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from numba import jit

start_time = time.time()

folder_path = "C:\Github\Aoc\\test_ding\participants"
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
data_frames = {}
for file in csv_files[:]:  # Limit to the first 3 files
    file_path = os.path.join(folder_path, file)
    data_frames[file] = pd.read_csv(file_path, header=None, names=['x', 'y'])

# define variables
x_maximum = 30
y_maximum = 50
points = [(672, 110),
          (1248, 110),
          (635, 970),
          (1214, 970),
          (961, 540),
          (97, 110),
          (1825, 110),
          (97, 970),
          (1787, 970)]
rectangles = {f'p{i + 1}': (point[0] - x_maximum, point[0] + x_maximum, point[1] - y_maximum, point[1] + y_maximum)
              for i, point in enumerate(points)}
trial_size = 20000  # Trial size, 20,000 points per trial


@jit(nopython=True)
def check_if_point_in_rectangle(x, y, rect):
    """Check if a point (x, y) lies within the rectangle described by its corner points."""
    min_x, max_x, min_y, max_y = rect
    return min_x <= x <= max_x and min_y <= y <= max_y


# Loading in the data
for file, df in data_frames.items():
    df['x'] = df['x'].interpolate(method='linear', limit_direction='both').round().astype('int16')
    df['y'] = df['y'].interpolate(method='linear', limit_direction='both').round().astype('int16')


for participant, df in data_frames.items():
    num_trials = len(df) // trial_size
    df_new = pd.DataFrame()

    for trial_idx in range(num_trials):
        start_idx = trial_idx * trial_size
        end_idx = (trial_idx + 1) * trial_size

        trial_df = df.iloc[start_idx:end_idx]

        # Initialize variables to track which rectangle is being checked
        walk_through_points = 0  # This will track which rectangle we're checking
        indices_to_delete = []  # To store the indices of the points to delete
        all_rectangles_found = False  # Flag to check if all rectangles are found

        for point_idx, (x, y) in enumerate(zip(trial_df['x'], trial_df['y'])):
            if check_if_point_in_rectangle(x, y, rectangles[f"p{walk_through_points + 1}"]):
                walk_through_points += 1

            if walk_through_points == 9:
                all_rectangles_found = True
                break

        if not all_rectangles_found:
            continue
            # print(participant, walk_through_points, start_idx, end_idx, 'Fail')
        else:
            # continue
            # print(participant, walk_through_points, start_idx, end_idx, 'Success')
            df_new = pd.concat([df_new, trial_df], axis=0)
    data_frames[participant] = df_new


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.2f}seconds")

#
# # # Iterate through all data points
# # point_idx = 0  # Start from the first data point
# # walk_through_points = 0  # This will track which rectangle we're checking
#
# # # Loop through each rectangle from p1 to p9
# # while walk_through_points < 9 and point_idx < len(df):
# #     # Get the current point
# #     x, y = df.iloc[point_idx]['x'], df.iloc[point_idx]['y']
#
# #     # Get the rectangle being checked
# #     rect_name = f"p{walk_through_points + 1}"  # p1, p2, ..., p9
# #     rect = rectangles[rect_name]
#
#
# #     # Check if the point is within the current rectangle
# #     if check_if_point_in_rectangle(x, y, rect):
# #         print(f"Data point {point_idx} ({x}, {y}) found in {rect_name}.")
# #         walk_through_points += 1  # Move to the next rectangle
#
# #     # Move to the next point in the DataFrame
# #     point_idx += 1
#
# # # After finishing the loop, check if all rectangles were matched
# # if walk_through_points == 9:
# #     print("All rectangles matched in sequence!")
# # else:
# #     print(f"Stopped after {walk_through_points} rectangles.")
#
#
# # ========================================================================================================
# # ============================ SAVING NEW DATA ==================================================================
# # ========================================================================================================
# # save_path = "C://Users//bjorn//OneDrive//Documenten//TU Delft WB//MSc-ME-BMD//Human Robot Interaction//Assignment 2//Q1_updated"
#
# # # Ensure the directory exists
# # os.makedirs(save_path, exist_ok=True)
#
# # # Iterate over chunked_data_frames for each participant
# # for i, (list_name, chunk_list) in enumerate(chunked_data_frames.items()):
# #     # Combine all chunks for the current participant into one DataFrame
# #     combined_df = pd.concat(chunk_list, ignore_index=True)
#
# #     # Define the file name for each chunk (e.g., participant_1_updated.csv, participant_2_updated.csv)
# #     file_name = f"participant_{i + 1}_updated.csv"
#
# #     # Define the full path to save the file
# #     file_path = os.path.join(save_path, file_name)
#
# #     # Save the DataFrame to a CSV file
# #     combined_df.to_csv(file_path, header = False, index=False)
# #     print(f"Saved combined data for participant {i + 1} as {file_name}")
#
# # ========================================================================================================
# # ============================ PLOTTING ==================================================================
# # ========================================================================================================
#
# fig, ax = plt.subplots(figsize=(8, 6))  # Set the figure size (optional)
# plt.plot(df['x'], df['y'], linestyle='-', color='green', alpha=0.5,
#          label=f"Data from {file}")  # Plot x vs y with markers
#
# # Plotting the rectangle around numbers 1-9
# for idx, (x, y) in enumerate(points):
#     ax.scatter(x, y, color='red', s=1, label=f'P{idx + 1}' if idx == 0 else "")  # Mark points
#     # Add a rectangle outline around each point
#     rect = patches.Rectangle(
#         (x - x_maximum, y - y_maximum),  # Bottom-left corner of the rectangle
#         2 * x_maximum,  # Width
#         2 * y_maximum,  # Height
#         linewidth=1, edgecolor='blue', facecolor='none'  # Outline properties
#     )
#     ax.add_patch(rect)
#
# for idx, (x, y) in enumerate(points, start=1):
#     ax.text(x + 20, y + 30, f'{idx}', color='blue', fontsize=12)  # Label the point
#
# # Plotting the 'screen'
# rect = patches.Rectangle((0, 0), 1920, 1080, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.1)
# ax.add_patch(rect)
#
# # Add titles and labels
# plt.title(f"Plot of x vs y from {file}")
# plt.xlabel('x')
# plt.ylabel('y')
# ax.set_xlim(-500, 2500)
# ax.set_ylim(-50, 2000)
#
# # Show the legend & plot
# plt.grid()
# plt.legend()
# plt.show()
#
# # ========================================================================================================
# # ============================ PRINT RUNTIME =============================================================
# # ========================================================================================================
#
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Code execution time: {elapsed_time:.2f} seconds")