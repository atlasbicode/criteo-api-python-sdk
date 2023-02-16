# CreateUserBehaviorSegmentV2

Inclusive and exclusive segments of a user behavior audience 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_action** | **str** | Type of shopper activity used to generate the audience. | 
**lookback_window** | **str** | Length of lookback window | 
**category_ids** | **[str]** | The categories to target | [optional] 
**brand_ids** | **[str]** | The brands to target | [optional] 
**min_price** | **float** | The min price of targeted skus. | [optional] [readonly] 
**max_price** | **float** | The max price of targeted skus. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

