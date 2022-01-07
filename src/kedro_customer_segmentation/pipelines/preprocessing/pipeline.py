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
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.17.5
"""

from kedro.pipeline import Pipeline, node
from .nodes.create_data_nb_products_per_basket import create_data_nb_products_per_basket
from .nodes.create_to_canceled import create_to_canceled
from .nodes.drop_to_canceled import drop_to_canceled
from .nodes.add_column_TotalPrice import add_column_TotalPrice
from .nodes.create_df_produits import create_df_produits
from .nodes.keywords_inventory import keywords_inventory
from .nodes.create_matrix import create_matrix
from .nodes.creating_clusters_products import creating_clusters_products
from .nodes.create_customer_categories import create_customer_categories




def create_preprocessing_pipeline(**kwargs):
    return Pipeline([
        node(
         		func=create_data_nb_products_per_basket,
         		inputs=["data_drop_duplicates"],
                outputs= "data_nb_products_per_basket",
         		name="create_data_nb_products_per_basket"
            ),
        node(
         		func=create_to_canceled,
         		inputs=["data_drop_duplicates"],
                outputs= ["data_quantity_canceled","entry_to_remove","doubtfull_entry"],
         		name="create_to_canceled"
            ),
        node(
         		func=drop_to_canceled,
         		inputs=["data_quantity_canceled","entry_to_remove","doubtfull_entry"],
                outputs= "data_drop_canceled",
         		name="drop_to_canceled"
            ),
        node(
         		func=add_column_TotalPrice,
         		inputs=["data_drop_canceled"],
                outputs= "data_TotalPrice",
         		name="add_column_TotalPrice"
            ),
        node(
         		func=create_df_produits,
         		inputs=["data_TotalPrice"],
                outputs= "df_produits",
         		name="create_df_produits"
            ),
        node(
         		func=keywords_inventory,
         		inputs=["df_produits"],
                outputs= ["keywords", "keywords_select", "count_keywords"],
         		name="keywords_inventory"
            ),
        node(
         		func=create_matrix,
         		inputs=["data_TotalPrice","count_keywords","keywords_select"],
                outputs= "matrix",
         		name="create_matrix"
            ),
        node(
         		func=creating_clusters_products,
         		inputs=["matrix"],
                outputs= "clusters_products",
         		name="creating_clusters_products"
            ),
        node(
         		func=create_customer_categories,
         		inputs=["data_TotalPrice","clusters_products"],
                outputs= "selected_customers",
         		name="create_customer_categories"
            )
            
         	
    ])


