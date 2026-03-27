import pandas as pd
import sklearn as sklearn
import matplotlib as plt

df = pd.read_csv("data/fgMILB.csv")

# sort properly
df = df.sort_values(by=["PlayerId", "Season"])
war_df = pd.read_csv("data/fgCWAR.csv")

# keep only what we need
war_df = war_df[["PlayerId", "WAR"]]

players = []

for pid, group in df.groupby("PlayerId"):
    total_pa = 0

    stats = {"PA": 0, "K%": 0, "BB%": 0, "ISO": 0, "wRC+": 0, "Age": 0}

    for _, row in group.iterrows():
        if total_pa >= 200:
            break

        pa = row["PA"]
        use_pa = min(pa, 200 - total_pa)

        stats["PA"] += use_pa
        stats["K%"] += row["K%"] * use_pa
        stats["BB%"] += row["BB%"] * use_pa
        stats["ISO"] += row["ISO"] * use_pa
        stats["wRC+"] += row["wRC+"] * use_pa
        stats["Age"] += row["Age"] * use_pa

        total_pa += use_pa

    if total_pa == 200:
        players.append(
            {
                "PlayerId": pid,
                "PA": 200,
                "K%": stats["K%"] / 200,
                "BB%": stats["BB%"] / 200,
                "ISO": stats["ISO"] / 200,
                "wRC+": stats["wRC+"] / 200,
                "Age": stats["Age"] / 200,
            }
        )

df_200 = pd.DataFrame(players)
df_200 = df_200[df_200["Age"] <= 26]

# make sure types match
df_200["PlayerId"] = df_200["PlayerId"].astype(str)
war_df["PlayerId"] = war_df["PlayerId"].astype(str)


# merge MILB stats with MLB WAR
df_final = df_200.merge(war_df, on="PlayerId", how="left")

# players who never made MLB
df_final["WAR"] = df_final["WAR"].fillna(0)

# success label
df_final["success"] = (df_final["WAR"] > 5).astype(int)

# print(df_final.shape)
# print(df_final["success"].value_counts())
df_final.head()
df_final.to_csv("data/final_dataset2.csv", index=False)
# print(df_200["PA"].value_counts())
# print(df_final["WAR"].describe())
# print(df_final["success"].mean())

print(df_200["Age"].max())
print(df_200[df_200["Age"] > 26].head())
print((df_200["Age"] > 26).sum())
# print(len(df_200))
