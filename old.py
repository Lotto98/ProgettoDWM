def outliers_remove(merged_prop,logerror):
    n_row=logerror.shape[0]
    value_count=logerror['logerror'].value_counts().sort_index(ascending=True)

    left=0
    right=0

    no_outliers_left=[]
    no_outliers_right=[]

    for i in value_count.index:
        
        if left+(value_count.loc[i]/n_row)<0.025:
            left=left+(value_count.loc[i]/n_row)

        else:
            no_outliers_left.append(i)
    
    for i in value_count.index[::-1]:
        
        if right+(value_count.loc[i]/n_row)<0.025:
            right=right+(value_count.loc[i]/n_row)
        
        else:
            no_outliers_right.append(i)
                
    no_outliers=list(set(no_outliers_left) & set(no_outliers_right))

    logerror_outlierfree=logerror[logerror['logerror'].isin(no_outliers)]

    fig,ax=plt.subplots(figsize=(30,10))
    logerror_outlierfree['logerror'].value_counts().plot(ax=ax, kind="line", xlabel='numbers', ylabel='frequency')

    merged_prop_outlierfree=merged_prop.iloc[logerror_outlierfree.index]

    print("N outlier rimossi: ",logerror.shape[0]-logerror_outlierfree.shape[0])
    
    return merged_prop_outlierfree,logerror_outlierfree

#train_X,train_Y=outliers_remove(train_X,train_Y)