#Top 10 Anime based on user rating
def graph(p):
    plt.figure(figsize =(18,6))
    top_10 = df.copy()
    top_10 = (top_10.groupby(by = ['anime_title'])[p].
     count().
     reset_index()
    [['anime_title', p]]
    )
     

    top_10= top_10[['anime_title', p]].sort_values(by = p,ascending = False).head(10)
    s = sns.barplot(x="anime_title", y=p, data = top_10, palette = 'magma', edgecolor = 'w')
    s.set_xticklabels(s.get_xticklabels(), fontsize=12, rotation=40, ha="right")

    s.set_title('Top 10 Anime based on ratings',fontsize = 22)
    s.set_xlabel('Anime',fontsize = 20) 
    s.set_ylabel(p, fontsize = 20)

