# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is a boilerplate pipeline 'machine_learning'
generated using Kedro 0.17.5
"""
from kedro_customer_segmentation.pipelines import Pipeline, node
from .nodes.SVC import svc
from .nodes.Logistic_Regression import lr
from .nodes.tree import tree
from .nodes.data_split import data_split

def create_Machine_Learning_pipeline(**kwargs):
    return Pipeline(
        [
			 node(
				func=svc,
         		inputs=["X_train","Y_train","X_test","Y_test"],
                outputs= "svc_results",
         		name="svc"
			 ),
             node(
                func=lr,
                inputs=["X_train","Y_train","X_test","Y_test"],
                outputs= "lr_results",
         		name="lr"
             ),
             node(
                func=tree,
                inputs=["X_train","Y_train","X_test","Y_test"],
                outputs= "lr_results",
         		name="lr"
             ),
             node(
                
                func=data_split,
                inputs=["selected_customers"],
                outputs=["X_train", "X_test", "Y_train", "Y_test"],
         		name="lr"


             )
			 
        ]
    )
