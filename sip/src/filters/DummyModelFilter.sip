class DummyModelFilter : public ModelFilter, public INeedExperimentEnvironment, public Initializable {
  %TypeHeaderCode
  #include "filters/DummyModelFilter.h"
  %End
  public:
    DummyModelFilter();
    void run(RecDat* rec_dat);
    //vector<pair<int,double> >* get_global_users();
    //vector<pair<int,double> >* get_global_items();
    void set_experiment_environment(ExperimentEnvironment* experiment_environment);
    void set_users(std::vector<int>* users);
    void set_users(VectorInt);
    %MethodCode
        sipCpp->set_users(&(a0->vec));
    %End
    void set_items(std::vector<int>* items);
    void set_items(VectorInt);
    %MethodCode
        sipCpp->set_items(&(a0->vec));
    %End
    bool init();
    bool self_test();
};
