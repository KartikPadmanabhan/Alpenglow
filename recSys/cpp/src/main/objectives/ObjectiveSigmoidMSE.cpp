/*
 * ObjectiveSigmoidMSE.cpp
 *
 *  Created on: 2014.04.15.
 *      Author: kisstom
 */

#include "ObjectiveSigmoidMSE.h"

double ObjectiveSigmoidMSE::get_gradient(RecPred* rec_pred) {
  return (rec_pred->prediction - rec_pred->score) *
      Util::logistic_function(rec_pred->prediction);
}


