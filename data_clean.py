import os
import pandas as pd

path = "./raw_data"

raw_data_files = os.listdir(path)
data_files_full_path = list(map(lambda file: path + '/' + file, raw_data_files))

raw_data = []

for file in data_files_full_path:
    df = pd.read_csv(file, index_col=None, header=0)
    raw_data.append(df)

raw_df = pd.concat(raw_data, axis=0, ignore_index=True)
extra_cols = ["version", "bright_t31", "frp", "daynight", "type"]

for col in extra_cols:
    raw_df = raw_df.drop(col, axis=1)

final_df = raw_df[(raw_df.confidence > 75)]
final_df = final_df[(final_df.latitude > -22.268764) & (final_df.latitude < -0.878872)]
final_df = final_df[(final_df.longitude > 8.795462) & (final_df.longitude < 42.363833)]

print(final_df)
final_df.to_csv("confidence_75.csv", index=False)

final_df = raw_df[(raw_df.confidence > 80)]
final_df = final_df[(final_df.latitude > -22.268764) & (final_df.latitude < -0.878872)]
final_df = final_df[(final_df.longitude > 8.795462) & (final_df.longitude < 42.363833)]

print(final_df)
final_df.to_csv("confidence_80.csv", index=False)

final_df = raw_df[(raw_df.confidence > 85)]
final_df = final_df[(final_df.latitude > -22.268764) & (final_df.latitude < -0.878872)]
final_df = final_df[(final_df.longitude > 8.795462) & (final_df.longitude < 42.363833)]

print(final_df)
final_df.to_csv("confidence_85.csv", index=False)

final_df = raw_df[(raw_df.confidence > 90)]
final_df = final_df[(final_df.latitude > -22.268764) & (final_df.latitude < -0.878872)]
final_df = final_df[(final_df.longitude > 8.795462) & (final_df.longitude < 42.363833)]

print(final_df)
final_df.to_csv("confidence_90.csv", index=False)

final_df = raw_df[(raw_df.confidence > 95)]
final_df = final_df[(final_df.latitude > -22.268764) & (final_df.latitude < -0.878872)]
final_df = final_df[(final_df.longitude > 8.795462) & (final_df.longitude < 42.363833)]

print(final_df)
final_df.to_csv("confidence_95.csv", index=False)