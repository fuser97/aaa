# Radar Chart (Spider Plot) for Mass/Volume Ratios
st.markdown("### Radar Chart (Spider Plot) for Mass/Volume Ratios")
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Ottieni tutte le combinazioni di fase e tipo di liquido
phases_liquids = mass_volume_df[["Phase", "Liquid Type"]].drop_duplicates().values.tolist()
num_vars = len(phases_liquids)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Chiude il radar chart

# Aggiungi i dati per ogni fonte (scenario o letteratura)
for source in mass_volume_df["Source"].unique():
    source_data = mass_volume_df[mass_volume_df["Source"] == source]
    data = [
        source_data[
            (source_data["Phase"] == phase) & (source_data["Liquid Type"] == liquid)
        ]["S/L Ratio"].sum()
        for phase, liquid in phases_liquids
    ]
    data += data[:1]  # Chiude il radar plot
    ax.plot(angles, data, label=source, linewidth=2)
    ax.fill(angles, data, alpha=0.25)

# Configura le etichette
labels = [f"{phase}\n({liquid})" for phase, liquid in phases_liquids]
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)

ax.set_title("Mass/Volume Ratios by Phase and Liquid")
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1))
st.pyplot(fig)
