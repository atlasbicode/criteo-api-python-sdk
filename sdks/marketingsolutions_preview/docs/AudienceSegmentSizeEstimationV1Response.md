# AudienceSegmentSizeEstimationV1Response

Represents an API response message containing the usual outcome fields (warnings+errors), and a valueResource data,  i.e. data is not an entity (no id). This can be used for association objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AudienceSegmentSizeEstimationV1Resource**](AudienceSegmentSizeEstimationV1Resource.md) |  | [optional] 
**warnings** | [**[CommonProblem]**](CommonProblem.md) |  | [optional] [readonly] 
**errors** | [**[CommonProblem]**](CommonProblem.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

