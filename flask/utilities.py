import pandas as pd
import numpy
from sklearn.preprocessing import normalize 

feature_list = pd.read_csv('feature_list_df.csv')
feature_list = feature_list.values[:,1].tolist()
#print feature_list
pca_components = pd.read_csv('pca_components_df.csv')
pca_components = pca_components.values[:,1:]
document_matrix_pca_transformed_norm = \
    pd.read_csv('document_matrix_pca_transformed_norm_df.csv')
document_matrix_pca_transformed_norm = document_matrix_pca_transformed_norm.values[:,1:]
#print document_matrix_pca_transformed_norm.shape
#print pca_components.shape
links_ = pd.read_csv('links_df.csv')
links_ = links_.values[:,1]
#print links_.shape
joined_token_list = pd.read_csv('joined_token_list_df.csv')
joined_token_list = joined_token_list.values[:,1]
#print joined_token_list.shape


#print "======> OMG LOOK AT THIS SHIT"
#print links_[0:10]
#print feature_list[100:200]
#print pca_components[:10,:10]
#print document_matrix_pca_transformed_norm[:10, :10]


def similarity(input_word):
    try:
        index_feature = feature_list.index(input_word)
    except:
        print "ERROR MESSAGE"
        return "error_message"
    
    input_projection_pca = pca_components[:,index_feature]
    #print input_projection_pca
    input_projection_pca = normalize(input_projection_pca, norm='l2', axis=1, 
        copy=True)

    def cosine_similarity(array2):
        return numpy.dot(numpy.squeeze(input_projection_pca), array2)
    
    similarity_score = numpy.apply_along_axis(cosine_similarity, axis=1, 
        arr=document_matrix_pca_transformed_norm)

    similarity_df = pd.DataFrame({'link': links_,
                              'description': joined_token_list,
                              'sim_score': similarity_score})
    index_sorted_by_similarity = \
        similarity_df['sim_score'].sort(inplace=False, ascending=False).index

    # similarity_df_sorted = similarity_df.loc[index_sorted_by_similarity]
    # print similarity_df_sorted.head()
    


    similarity_df_sorted = similarity_df.sort_values('sim_score', ascending=False)
    print 'please be the same'
    print similarity_df_sorted.head()
    deduplicated = similarity_df_sorted.drop_duplicates(['description'])
    #pd.options.display.max_colwidth = 2000
    
    deduplicated = deduplicated[deduplicated.link!='None']
    p  = deduplicated['link'].values.tolist()
    
    return p[0:20]