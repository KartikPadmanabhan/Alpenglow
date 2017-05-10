#ifndef PREDICTION_CREATOR
#define PREDICTION_CREATOR
//TODO rename to toplistcreator/globaltoplistcreator/usertoplistcreator
#include <climits>
#include <iostream>
#include <gtest/gtest_prod.h>
#include "../utils/MinHeap.h"
#include "../models/Model.h"
#include "../filters/ModelFilter.h"

using namespace std;

struct PredictionCreatorParameters{
  int topK; //TODO top_k
  int lookback;
};
class PredictionCreator{
 public:
   PredictionCreator(PredictionCreatorParameters* params){
     top_k_ = params->topK; //TODO const
     lookback_ = params->lookback;
     model_ = NULL;
     filter_ = NULL;
     train_matrix_ = NULL;
   }
   virtual ~PredictionCreator(){}
   virtual vector<RecDat>* run(RecDat* rec_dat)=0; 
   void setModel(Model* model){model_=model;}; //TODO google code
   void setFilter(ModelFilter* filter){filter_=filter;} //TODO alternative: items or popsortedcont
   void setTrainMatrix(SpMatrix *train_matrix){train_matrix_ = train_matrix; }
   bool self_test(){
     bool OK = true;
     if(model_==NULL){
       OK = false;
       cerr << "Not set: Model of PredictionCreator." << endl;
     }
     if(filter_==NULL){
       OK = false;
       cerr << "Not set: Filter of PredictionCreator." << endl;
     }
     if(top_k_<=0){
       OK = false;
       cerr << "Invalid value top_k_==" << top_k_ << " is set in PredictionCreator." << endl;
     }
     if(lookback_==1 and train_matrix_==NULL){
       OK = false;
       cerr << "Not set: trainMatrix of PredictionCreator." << endl;
     }
     return OK;
   }
   bool selfTest(){ return self_test(); } //deprecated
 protected:
   vector<RecDat> top_predictions_;
   Model* model_;
   ModelFilter* filter_;
   SpMatrix* train_matrix_;
   int top_k_; //TODO const
   int lookback_;
};

struct PredictionCreatorGlobalParameters : public PredictionCreatorParameters{
  int initialThreshold; //TODO initial_threshold
};

class PredictionCreatorGlobal: public PredictionCreator{
  public:
    PredictionCreatorGlobal(PredictionCreatorGlobalParameters* params):PredictionCreator(params){
      min_heap_ = new MinHeap(params->topK); //TODO use utils/Toplist
      initial_threshold_ = (uint)params->initialThreshold;
    };
    virtual ~PredictionCreatorGlobal(){ delete min_heap_; }
    vector<RecDat>* run(RecDat* rec_dat);
    bool selfTest(){ return self_test(); }
    bool self_test(){
      bool OK = PredictionCreator::self_test(); 
      if(initial_threshold_ < 0){
        OK = false;
        cerr << "Invalid value initialThreshold=" << initial_threshold_ << " is set in PredictionCreatorGlobal." << endl;
      }
      return OK;
    }
  
  private:
    MinHeap* min_heap_;
    uint initial_threshold_;
    //void process_row(vector<pair<int,double> >* sortedEntitiesA,uint startIndexA,int indexB,RecDat* recDat,uint threshold);
    //void process_column(vector<pair<int,double> >* sortedEntitiesA,uint startIndexA,int indexB,RecDat* recDat,uint threshold);


    void process_line(vector<pair<int,double> >* sortedAs,uint beginAIndex, uint endAIndex, int* _recDat_a, RecDat* _recDat);
    void process_rectangle(vector<pair<int,double> >* sortedUsers, vector<pair<int,double> >* sortedItems, uint beginUserIndex, uint beginItemIndex, uint endUserIndex, uint endItemIndex, RecDat* _recDat);
    FRIEND_TEST(TestPredictionCreatorGlobal, global);
    FRIEND_TEST(TestPredictionCreatorGlobal, global2);
    FRIEND_TEST(TestPredictionCreatorGlobal, processLine);
    FRIEND_TEST(TestPredictionCreatorGlobal, processLine2);
    FRIEND_TEST(TestPredictionCreatorGlobal, processSquare);
    FRIEND_TEST(TestPredictionCreatorGlobal, lookback);
};

struct PredictionCreatorPersonalizedParameters : public PredictionCreatorParameters{
};
class PredictionCreatorPersonalized: public PredictionCreator{
  public:
    PredictionCreatorPersonalized(PredictionCreatorParameters * params):PredictionCreator(params){
      min_heap_ = new MinHeap(params->topK); //TODO use utils/Toplist
    };
    vector<RecDat>* run(RecDat* rec_dat);
    bool self_test(){ return PredictionCreator::self_test(); }
  private:
    MinHeap* min_heap_;
};

#endif
