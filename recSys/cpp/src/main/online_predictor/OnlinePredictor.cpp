#include "OnlinePredictor.h"

void OnlinePredictor::set_parameters(OnlinePredictorParameters * params){
  min_time = params->min_time;
  time_frame = params->time_frame;
  ofs.open(params->file_name.c_str());
  pastTimeFrame = 0;
  actualTimeFrame = 0;
  predictionCreator=NULL;
}

void OnlinePredictor::run(RecDat * rec_dat){
  if(doPredict(rec_dat)){
    cerr << "OnlinePredictor::predict computes prediction." << endl;
    vector<RecDat>* topPredictions = predictionCreator->run(rec_dat);
    for(uint ii=0; ii<topPredictions->size(); ii++){
      ofs << actualTimeFrame << " " << topPredictions->at(ii).user << " " << topPredictions->at(ii).item << " " << topPredictions->at(ii).score << endl; 
    } 
    cerr << "OnlinePredictor::predict done" << endl;
  }
}

bool OnlinePredictor::doPredict(RecDat * rec_dat){
  double actualTime = rec_dat->time;
  actualTimeFrame = (int)(actualTime - min_time)/(time_frame);
  if(actualTime > min_time && actualTimeFrame !=pastTimeFrame){
    pastTimeFrame = actualTimeFrame;
    return true;
  }
  else return false;
}
