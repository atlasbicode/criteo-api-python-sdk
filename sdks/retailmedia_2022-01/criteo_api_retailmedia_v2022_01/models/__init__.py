# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from criteo_api_retailmedia_v2022_01.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_retailmedia_v2022_01.model.access_token_model import AccessTokenModel
from criteo_api_retailmedia_v2022_01.model.add_to_basket_ids_update_model202110_request import AddToBasketIdsUpdateModel202110Request
from criteo_api_retailmedia_v2022_01.model.add_to_basket_target202110_request import AddToBasketTarget202110Request
from criteo_api_retailmedia_v2022_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from criteo_api_retailmedia_v2022_01.model.application_summary_model import ApplicationSummaryModel
from criteo_api_retailmedia_v2022_01.model.application_summary_model_resource import ApplicationSummaryModelResource
from criteo_api_retailmedia_v2022_01.model.application_summary_model_response import ApplicationSummaryModelResponse
from criteo_api_retailmedia_v2022_01.model.auction_line_item_create_model_request import AuctionLineItemCreateModelRequest
from criteo_api_retailmedia_v2022_01.model.auction_line_item_paged_list_response import AuctionLineItemPagedListResponse
from criteo_api_retailmedia_v2022_01.model.auction_line_item_response import AuctionLineItemResponse
from criteo_api_retailmedia_v2022_01.model.auction_line_item_update_model_request import AuctionLineItemUpdateModelRequest
from criteo_api_retailmedia_v2022_01.model.audience_ids_update_model202110_request import AudienceIdsUpdateModel202110Request
from criteo_api_retailmedia_v2022_01.model.audience_target202110_request import AudienceTarget202110Request
from criteo_api_retailmedia_v2022_01.model.audience_target202110_response import AudienceTarget202110Response
from criteo_api_retailmedia_v2022_01.model.bad_request import BadRequest
from criteo_api_retailmedia_v2022_01.model.balance202110_paged_list_response import Balance202110PagedListResponse
from criteo_api_retailmedia_v2022_01.model.balance_campaign202110_list_request import BalanceCampaign202110ListRequest
from criteo_api_retailmedia_v2022_01.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from criteo_api_retailmedia_v2022_01.model.common_error import CommonError
from criteo_api_retailmedia_v2022_01.model.common_line_item_paged_list_response import CommonLineItemPagedListResponse
from criteo_api_retailmedia_v2022_01.model.common_line_item_response import CommonLineItemResponse
from criteo_api_retailmedia_v2022_01.model.common_problem import CommonProblem
from criteo_api_retailmedia_v2022_01.model.common_warning import CommonWarning
from criteo_api_retailmedia_v2022_01.model.create_audience_body import CreateAudienceBody
from criteo_api_retailmedia_v2022_01.model.create_audience_request import CreateAudienceRequest
from criteo_api_retailmedia_v2022_01.model.create_retail_media_audience_response import CreateRetailMediaAudienceResponse
from criteo_api_retailmedia_v2022_01.model.creative202110 import Creative202110
from criteo_api_retailmedia_v2022_01.model.creative202110_list_response import Creative202110ListResponse
from criteo_api_retailmedia_v2022_01.model.envelope_report_request import EnvelopeReportRequest
from criteo_api_retailmedia_v2022_01.model.envelope_report_status import EnvelopeReportStatus
from criteo_api_retailmedia_v2022_01.model.error import Error
from criteo_api_retailmedia_v2022_01.model.external_account import ExternalAccount
from criteo_api_retailmedia_v2022_01.model.external_add_to_basket_ids_update_model202110 import ExternalAddToBasketIdsUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.external_add_to_basket_target202110 import ExternalAddToBasketTarget202110
from criteo_api_retailmedia_v2022_01.model.external_auction_line_item import ExternalAuctionLineItem
from criteo_api_retailmedia_v2022_01.model.external_auction_line_item_create_model import ExternalAuctionLineItemCreateModel
from criteo_api_retailmedia_v2022_01.model.external_auction_line_item_update_model import ExternalAuctionLineItemUpdateModel
from criteo_api_retailmedia_v2022_01.model.external_audience_ids_update_model202110 import ExternalAudienceIdsUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.external_audience_target202110 import ExternalAudienceTarget202110
from criteo_api_retailmedia_v2022_01.model.external_balance202110 import ExternalBalance202110
from criteo_api_retailmedia_v2022_01.model.external_brand import ExternalBrand
from criteo_api_retailmedia_v2022_01.model.external_campaign import ExternalCampaign
from criteo_api_retailmedia_v2022_01.model.external_campaign_attributes import ExternalCampaignAttributes
from criteo_api_retailmedia_v2022_01.model.external_catalog_request import ExternalCatalogRequest
from criteo_api_retailmedia_v2022_01.model.external_catalog_status import ExternalCatalogStatus
from criteo_api_retailmedia_v2022_01.model.external_common_line_item import ExternalCommonLineItem
from criteo_api_retailmedia_v2022_01.model.external_editable_campaign_attributes import ExternalEditableCampaignAttributes
from criteo_api_retailmedia_v2022_01.model.external_keyword_target202110 import ExternalKeywordTarget202110
from criteo_api_retailmedia_v2022_01.model.external_line_item_capping202110 import ExternalLineItemCapping202110
from criteo_api_retailmedia_v2022_01.model.external_line_item_page202110 import ExternalLineItemPage202110
from criteo_api_retailmedia_v2022_01.model.external_line_item_page_category202110 import ExternalLineItemPageCategory202110
from criteo_api_retailmedia_v2022_01.model.external_post_campaign import ExternalPostCampaign
from criteo_api_retailmedia_v2022_01.model.external_preferred_line_item202110 import ExternalPreferredLineItem202110
from criteo_api_retailmedia_v2022_01.model.external_preferred_line_item_create_model202110 import ExternalPreferredLineItemCreateModel202110
from criteo_api_retailmedia_v2022_01.model.external_preferred_line_item_update_model202110 import ExternalPreferredLineItemUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.external_promoted_product202110 import ExternalPromotedProduct202110
from criteo_api_retailmedia_v2022_01.model.external_put_campaign import ExternalPutCampaign
from criteo_api_retailmedia_v2022_01.model.external_retailer import ExternalRetailer
from criteo_api_retailmedia_v2022_01.model.external_retailer_pages202110 import ExternalRetailerPages202110
from criteo_api_retailmedia_v2022_01.model.external_store_ids_update_model202110 import ExternalStoreIdsUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.external_store_target202110 import ExternalStoreTarget202110
from criteo_api_retailmedia_v2022_01.model.get_page_of_audiences_by_account_id_response import GetPageOfAudiencesByAccountIdResponse
from criteo_api_retailmedia_v2022_01.model.input_resource_of_auction_line_item_create_model import InputResourceOfAuctionLineItemCreateModel
from criteo_api_retailmedia_v2022_01.model.input_resource_of_preferred_line_item_create_model202110 import InputResourceOfPreferredLineItemCreateModel202110
from criteo_api_retailmedia_v2022_01.model.json_api_body_with_external_id_of_editable_campaign_attributes_and_campaign import JsonApiBodyWithExternalIdOfEditableCampaignAttributesAndCampaign
from criteo_api_retailmedia_v2022_01.model.json_api_body_with_id_of_int64_and_account_and_account import JsonApiBodyWithIdOfInt64AndAccountAndAccount
from criteo_api_retailmedia_v2022_01.model.json_api_body_with_id_of_int64_and_brand_and_brand import JsonApiBodyWithIdOfInt64AndBrandAndBrand
from criteo_api_retailmedia_v2022_01.model.json_api_body_with_id_of_int64_and_campaign_and_campaign import JsonApiBodyWithIdOfInt64AndCampaignAndCampaign
from criteo_api_retailmedia_v2022_01.model.json_api_body_with_id_of_int64_and_catalog_status_and_catalog_status import JsonApiBodyWithIdOfInt64AndCatalogStatusAndCatalogStatus
from criteo_api_retailmedia_v2022_01.model.json_api_body_with_id_of_int64_and_retailer_and_retailer import JsonApiBodyWithIdOfInt64AndRetailerAndRetailer
from criteo_api_retailmedia_v2022_01.model.json_api_body_without_id_of_campaign_attributes_and_campaign import JsonApiBodyWithoutIdOfCampaignAttributesAndCampaign
from criteo_api_retailmedia_v2022_01.model.json_api_body_without_id_of_catalog_request_and_catalog_request import JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequest
from criteo_api_retailmedia_v2022_01.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
from criteo_api_retailmedia_v2022_01.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from criteo_api_retailmedia_v2022_01.model.json_api_page_response_of_campaign import JsonApiPageResponseOfCampaign
from criteo_api_retailmedia_v2022_01.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
from criteo_api_retailmedia_v2022_01.model.json_api_request_of_catalog_request import JsonApiRequestOfCatalogRequest
from criteo_api_retailmedia_v2022_01.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from criteo_api_retailmedia_v2022_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_v2022_01.model.keyword_target202110_request import KeywordTarget202110Request
from criteo_api_retailmedia_v2022_01.model.keyword_target202110_response import KeywordTarget202110Response
from criteo_api_retailmedia_v2022_01.model.map_string import MapString
from criteo_api_retailmedia_v2022_01.model.o_auth_error_model import OAuthErrorModel
from criteo_api_retailmedia_v2022_01.model.page_metadata import PageMetadata
from criteo_api_retailmedia_v2022_01.model.preferred_line_item202110_paged_list_response import PreferredLineItem202110PagedListResponse
from criteo_api_retailmedia_v2022_01.model.preferred_line_item202110_response import PreferredLineItem202110Response
from criteo_api_retailmedia_v2022_01.model.preferred_line_item_create_model202110_request import PreferredLineItemCreateModel202110Request
from criteo_api_retailmedia_v2022_01.model.preferred_line_item_update_model202110_request import PreferredLineItemUpdateModel202110Request
from criteo_api_retailmedia_v2022_01.model.problem_details import ProblemDetails
from criteo_api_retailmedia_v2022_01.model.promoted_product202110_list_request import PromotedProduct202110ListRequest
from criteo_api_retailmedia_v2022_01.model.promoted_product202110_paged_list_response import PromotedProduct202110PagedListResponse
from criteo_api_retailmedia_v2022_01.model.report_request import ReportRequest
from criteo_api_retailmedia_v2022_01.model.report_request_attributes import ReportRequestAttributes
from criteo_api_retailmedia_v2022_01.model.report_status import ReportStatus
from criteo_api_retailmedia_v2022_01.model.report_status_attributes import ReportStatusAttributes
from criteo_api_retailmedia_v2022_01.model.resource_of_auction_line_item import ResourceOfAuctionLineItem
from criteo_api_retailmedia_v2022_01.model.resource_of_auction_line_item_update_model import ResourceOfAuctionLineItemUpdateModel
from criteo_api_retailmedia_v2022_01.model.resource_of_balance202110 import ResourceOfBalance202110
from criteo_api_retailmedia_v2022_01.model.resource_of_balance_campaign202110 import ResourceOfBalanceCampaign202110
from criteo_api_retailmedia_v2022_01.model.resource_of_common_line_item import ResourceOfCommonLineItem
from criteo_api_retailmedia_v2022_01.model.resource_of_creative202110 import ResourceOfCreative202110
from criteo_api_retailmedia_v2022_01.model.resource_of_preferred_line_item202110 import ResourceOfPreferredLineItem202110
from criteo_api_retailmedia_v2022_01.model.resource_of_preferred_line_item_update_model202110 import ResourceOfPreferredLineItemUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.resource_of_promoted_product202110 import ResourceOfPromotedProduct202110
from criteo_api_retailmedia_v2022_01.model.retail_media_audience import RetailMediaAudience
from criteo_api_retailmedia_v2022_01.model.retail_media_audience_attributes import RetailMediaAudienceAttributes
from criteo_api_retailmedia_v2022_01.model.store_ids_update_model202110_request import StoreIdsUpdateModel202110Request
from criteo_api_retailmedia_v2022_01.model.store_target202110_request import StoreTarget202110Request
from criteo_api_retailmedia_v2022_01.model.store_target202110_response import StoreTarget202110Response
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_add_to_basket_ids_update_model202110 import ValueTypeResourceOfAddToBasketIdsUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_add_to_basket_target202110 import ValueTypeResourceOfAddToBasketTarget202110
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_audience_ids_update_model202110 import ValueTypeResourceOfAudienceIdsUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_audience_target202110 import ValueTypeResourceOfAudienceTarget202110
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_keyword_target202110 import ValueTypeResourceOfKeywordTarget202110
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_store_ids_update_model202110 import ValueTypeResourceOfStoreIdsUpdateModel202110
from criteo_api_retailmedia_v2022_01.model.value_type_resource_of_store_target202110 import ValueTypeResourceOfStoreTarget202110
