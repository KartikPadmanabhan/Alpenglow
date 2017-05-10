#ifndef POPULARITY_NEGATIVE_SAMPLE_GENERATOR
#define POPULARITY_NEGATIVE_SAMPLE_GENERATOR

#include "NegativeSampleGenerator.h"
#include "../utils/PopContainers.h"
#include "../recommender_data/RecommenderDataIterator.h"

struct PopularityNegativeSampleGeneratorParameters{
  int negativeRate;
  int seed;
};

class PopularityNegativeSampleGenerator: public NegativeSampleGenerator{
  public:
    PopularityNegativeSampleGenerator(PopularityNegativeSampleGeneratorParameters* params){
      negativeRate = params->negativeRate; 
      random.set(params->seed);
    }
    vector<int>* generate(RecDat* recDat);
    void setPopContainer(PopContainer* popContainer_){popContainer = popContainer_;}
    void setTrainMatrix(SpMatrix* trainMatrix_){trainMatrix=trainMatrix_;}
    void setRecommenderDataIterator(RecommenderDataIterator* recommenderDataIterator_){recommenderDataIterator=recommenderDataIterator_;}
    void setItems(vector<int>* items_){items=items_;}
  private:
    PopContainer *popContainer;
    vector<int>* items;
    SpMatrix* trainMatrix;
    RecommenderDataIterator* recommenderDataIterator;
    Random random;
    int negativeRate;
};


#endif