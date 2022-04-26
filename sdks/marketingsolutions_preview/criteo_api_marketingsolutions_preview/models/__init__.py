# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from criteo_api_marketingsolutions_preview.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_marketingsolutions_preview.model.access_token_model import AccessTokenModel
from criteo_api_marketingsolutions_preview.model.ad import Ad
from criteo_api_marketingsolutions_preview.model.ad_list_response import AdListResponse
from criteo_api_marketingsolutions_preview.model.ad_resource import AdResource
from criteo_api_marketingsolutions_preview.model.ad_response import AdResponse
from criteo_api_marketingsolutions_preview.model.ad_set_category_bid import AdSetCategoryBid
from criteo_api_marketingsolutions_preview.model.ad_set_category_bid_list_response import AdSetCategoryBidListResponse
from criteo_api_marketingsolutions_preview.model.ad_set_category_bid_resource import AdSetCategoryBidResource
from criteo_api_marketingsolutions_preview.model.ad_set_delivery_limitations import AdSetDeliveryLimitations
from criteo_api_marketingsolutions_preview.model.ad_set_display_multiplier import AdSetDisplayMultiplier
from criteo_api_marketingsolutions_preview.model.ad_set_display_multiplier_list_response import AdSetDisplayMultiplierListResponse
from criteo_api_marketingsolutions_preview.model.ad_set_display_multiplier_resource import AdSetDisplayMultiplierResource
from criteo_api_marketingsolutions_preview.model.ad_set_frequency_capping import AdSetFrequencyCapping
from criteo_api_marketingsolutions_preview.model.ad_set_geo_location import AdSetGeoLocation
from criteo_api_marketingsolutions_preview.model.ad_set_search_filter import AdSetSearchFilter
from criteo_api_marketingsolutions_preview.model.ad_set_targeting import AdSetTargeting
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_rule import AdSetTargetingRule
from criteo_api_marketingsolutions_preview.model.ad_write import AdWrite
from criteo_api_marketingsolutions_preview.model.ad_write_request import AdWriteRequest
from criteo_api_marketingsolutions_preview.model.ad_write_resource import AdWriteResource
from criteo_api_marketingsolutions_preview.model.advertiser_creation_input import AdvertiserCreationInput
from criteo_api_marketingsolutions_preview.model.advertiser_creation_request import AdvertiserCreationRequest
from criteo_api_marketingsolutions_preview.model.advertiser_creation_response import AdvertiserCreationResponse
from criteo_api_marketingsolutions_preview.model.advertiser_dataset_list_response import AdvertiserDatasetListResponse
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.application_summary_model import ApplicationSummaryModel
from criteo_api_marketingsolutions_preview.model.application_summary_model_resource import ApplicationSummaryModelResource
from criteo_api_marketingsolutions_preview.model.application_summary_model_response import ApplicationSummaryModelResponse
from criteo_api_marketingsolutions_preview.model.attribute import Attribute
from criteo_api_marketingsolutions_preview.model.audience import Audience
from criteo_api_marketingsolutions_preview.model.audience_attributes import AudienceAttributes
from criteo_api_marketingsolutions_preview.model.audience_custom import AudienceCustom
from criteo_api_marketingsolutions_preview.model.audience_error import AudienceError
from criteo_api_marketingsolutions_preview.model.audience_name_description import AudienceNameDescription
from criteo_api_marketingsolutions_preview.model.audience_warning import AudienceWarning
from criteo_api_marketingsolutions_preview.model.audience_website_visitor import AudienceWebsiteVisitor
from criteo_api_marketingsolutions_preview.model.basic_audience_definition import BasicAudienceDefinition
from criteo_api_marketingsolutions_preview.model.batch_accepted_response import BatchAcceptedResponse
from criteo_api_marketingsolutions_preview.model.campaign import Campaign
from criteo_api_marketingsolutions_preview.model.campaign_list_response import CampaignListResponse
from criteo_api_marketingsolutions_preview.model.campaign_read_resource import CampaignReadResource
from criteo_api_marketingsolutions_preview.model.campaign_response import CampaignResponse
from criteo_api_marketingsolutions_preview.model.campaign_search_filters import CampaignSearchFilters
from criteo_api_marketingsolutions_preview.model.campaign_search_request import CampaignSearchRequest
from criteo_api_marketingsolutions_preview.model.campaign_spend_limit import CampaignSpendLimit
from criteo_api_marketingsolutions_preview.model.common_problem import CommonProblem
from criteo_api_marketingsolutions_preview.model.contactlist_amendment import ContactlistAmendment
from criteo_api_marketingsolutions_preview.model.contactlist_amendment_attributes import ContactlistAmendmentAttributes
from criteo_api_marketingsolutions_preview.model.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_api_marketingsolutions_preview.model.contactlist_operation import ContactlistOperation
from criteo_api_marketingsolutions_preview.model.contactlist_operation_attributes import ContactlistOperationAttributes
from criteo_api_marketingsolutions_preview.model.contactlist_with_attributes_amendment import ContactlistWithAttributesAmendment
from criteo_api_marketingsolutions_preview.model.contactlist_with_attributes_amendment_attributes import ContactlistWithAttributesAmendmentAttributes
from criteo_api_marketingsolutions_preview.model.contactlist_with_attributes_amendment_request import ContactlistWithAttributesAmendmentRequest
from criteo_api_marketingsolutions_preview.model.coupon import Coupon
from criteo_api_marketingsolutions_preview.model.coupon_list_response import CouponListResponse
from criteo_api_marketingsolutions_preview.model.coupon_resource import CouponResource
from criteo_api_marketingsolutions_preview.model.coupon_response import CouponResponse
from criteo_api_marketingsolutions_preview.model.coupon_supported_sizes import CouponSupportedSizes
from criteo_api_marketingsolutions_preview.model.coupon_supported_sizes_resource import CouponSupportedSizesResource
from criteo_api_marketingsolutions_preview.model.coupon_supported_sizes_response import CouponSupportedSizesResponse
from criteo_api_marketingsolutions_preview.model.create_ad_set import CreateAdSet
from criteo_api_marketingsolutions_preview.model.create_ad_set_audience_configuration import CreateAdSetAudienceConfiguration
from criteo_api_marketingsolutions_preview.model.create_ad_set_bidding import CreateAdSetBidding
from criteo_api_marketingsolutions_preview.model.create_ad_set_budget import CreateAdSetBudget
from criteo_api_marketingsolutions_preview.model.create_ad_set_geo_location import CreateAdSetGeoLocation
from criteo_api_marketingsolutions_preview.model.create_ad_set_request import CreateAdSetRequest
from criteo_api_marketingsolutions_preview.model.create_ad_set_resource import CreateAdSetResource
from criteo_api_marketingsolutions_preview.model.create_ad_set_schedule import CreateAdSetSchedule
from criteo_api_marketingsolutions_preview.model.create_ad_set_targeting import CreateAdSetTargeting
from criteo_api_marketingsolutions_preview.model.create_campaign import CreateCampaign
from criteo_api_marketingsolutions_preview.model.create_campaign_request import CreateCampaignRequest
from criteo_api_marketingsolutions_preview.model.create_campaign_resource import CreateCampaignResource
from criteo_api_marketingsolutions_preview.model.create_campaign_spend_limit import CreateCampaignSpendLimit
from criteo_api_marketingsolutions_preview.model.create_coupon import CreateCoupon
from criteo_api_marketingsolutions_preview.model.create_coupon_request import CreateCouponRequest
from criteo_api_marketingsolutions_preview.model.create_coupon_resource import CreateCouponResource
from criteo_api_marketingsolutions_preview.model.create_image_slide import CreateImageSlide
from criteo_api_marketingsolutions_preview.model.create_product_set_request import CreateProductSetRequest
from criteo_api_marketingsolutions_preview.model.creative import Creative
from criteo_api_marketingsolutions_preview.model.creative_list_response import CreativeListResponse
from criteo_api_marketingsolutions_preview.model.creative_logo import CreativeLogo
from criteo_api_marketingsolutions_preview.model.creative_resource import CreativeResource
from criteo_api_marketingsolutions_preview.model.creative_response import CreativeResponse
from criteo_api_marketingsolutions_preview.model.creative_write import CreativeWrite
from criteo_api_marketingsolutions_preview.model.creative_write_request import CreativeWriteRequest
from criteo_api_marketingsolutions_preview.model.creative_write_resource import CreativeWriteResource
from criteo_api_marketingsolutions_preview.model.criteo_api_error import CriteoApiError
from criteo_api_marketingsolutions_preview.model.criteo_api_error_v2 import CriteoApiErrorV2
from criteo_api_marketingsolutions_preview.model.criteo_api_warning import CriteoApiWarning
from criteo_api_marketingsolutions_preview.model.criteo_api_warning_v2 import CriteoApiWarningV2
from criteo_api_marketingsolutions_preview.model.custom_attribute import CustomAttribute
from criteo_api_marketingsolutions_preview.model.dataset import Dataset
from criteo_api_marketingsolutions_preview.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_api_marketingsolutions_preview.model.delete_audience_response import DeleteAudienceResponse
from criteo_api_marketingsolutions_preview.model.dynamic_attributes import DynamicAttributes
from criteo_api_marketingsolutions_preview.model.dynamic_write_attributes import DynamicWriteAttributes
from criteo_api_marketingsolutions_preview.model.entity_filter import EntityFilter
from criteo_api_marketingsolutions_preview.model.entity_of_portfolio_message import EntityOfPortfolioMessage
from criteo_api_marketingsolutions_preview.model.entity_v2_of_dataset import EntityV2OfDataset
from criteo_api_marketingsolutions_preview.model.entity_v2_of_object import EntityV2OfObject
from criteo_api_marketingsolutions_preview.model.entity_wrapper_of_targeting_entity import EntityWrapperOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_preview.model.error_description import ErrorDescription
from criteo_api_marketingsolutions_preview.model.error_message import ErrorMessage
from criteo_api_marketingsolutions_preview.model.fail_response import FailResponse
from criteo_api_marketingsolutions_preview.model.generate_categories_report_request import GenerateCategoriesReportRequest
from criteo_api_marketingsolutions_preview.model.generate_categories_report_request_attributes import GenerateCategoriesReportRequestAttributes
from criteo_api_marketingsolutions_preview.model.generate_categories_report_request_data import GenerateCategoriesReportRequestData
from criteo_api_marketingsolutions_preview.model.generate_creatives_report_request import GenerateCreativesReportRequest
from criteo_api_marketingsolutions_preview.model.generate_creatives_report_request_attributes import GenerateCreativesReportRequestAttributes
from criteo_api_marketingsolutions_preview.model.generate_creatives_report_request_data import GenerateCreativesReportRequestData
from criteo_api_marketingsolutions_preview.model.generate_top_products_report_request import GenerateTopProductsReportRequest
from criteo_api_marketingsolutions_preview.model.generate_top_products_report_request_attributes import GenerateTopProductsReportRequestAttributes
from criteo_api_marketingsolutions_preview.model.generate_top_products_report_request_data import GenerateTopProductsReportRequestData
from criteo_api_marketingsolutions_preview.model.get_audiences_response import GetAudiencesResponse
from criteo_api_marketingsolutions_preview.model.get_portfolio_response import GetPortfolioResponse
from criteo_api_marketingsolutions_preview.model.image_attributes import ImageAttributes
from criteo_api_marketingsolutions_preview.model.image_slide import ImageSlide
from criteo_api_marketingsolutions_preview.model.image_write_attributes import ImageWriteAttributes
from criteo_api_marketingsolutions_preview.model.installment import Installment
from criteo_api_marketingsolutions_preview.model.json_report_rows import JsonReportRows
from criteo_api_marketingsolutions_preview.model.list_available_industries_response import ListAvailableIndustriesResponse
from criteo_api_marketingsolutions_preview.model.loyalty_points import LoyaltyPoints
from criteo_api_marketingsolutions_preview.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_preview.model.new_audience import NewAudience
from criteo_api_marketingsolutions_preview.model.new_audience_attributes import NewAudienceAttributes
from criteo_api_marketingsolutions_preview.model.new_audience_request import NewAudienceRequest
from criteo_api_marketingsolutions_preview.model.new_audience_response import NewAudienceResponse
from criteo_api_marketingsolutions_preview.model.nillable_ad_set_targeting_rule import NillableAdSetTargetingRule
from criteo_api_marketingsolutions_preview.model.nillable_date_time import NillableDateTime
from criteo_api_marketingsolutions_preview.model.nillable_decimal import NillableDecimal
from criteo_api_marketingsolutions_preview.model.o_auth_error_model import OAuthErrorModel
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_response import OciBrandSafetyResponse
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_response_data import OciBrandSafetyResponseData
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_rule import OciBrandSafetyRule
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_segment import OciBrandSafetySegment
from criteo_api_marketingsolutions_preview.model.oci_targeting_node import OciTargetingNode
from criteo_api_marketingsolutions_preview.model.oci_targeting_response import OciTargetingResponse
from criteo_api_marketingsolutions_preview.model.oci_targeting_response_data import OciTargetingResponseData
from criteo_api_marketingsolutions_preview.model.oci_targeting_rule import OciTargetingRule
from criteo_api_marketingsolutions_preview.model.ok_response import OkResponse
from criteo_api_marketingsolutions_preview.model.on_site_reco_request import OnSiteRecoRequest
from criteo_api_marketingsolutions_preview.model.on_site_reco_response import OnSiteRecoResponse
from criteo_api_marketingsolutions_preview.model.outcome import Outcome
from criteo_api_marketingsolutions_preview.model.patch_ad_set import PatchAdSet
from criteo_api_marketingsolutions_preview.model.patch_ad_set_bidding import PatchAdSetBidding
from criteo_api_marketingsolutions_preview.model.patch_ad_set_budget import PatchAdSetBudget
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid import PatchAdSetCategoryBid
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid_list_request import PatchAdSetCategoryBidListRequest
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid_resource import PatchAdSetCategoryBidResource
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid_result_list_response import PatchAdSetCategoryBidResultListResponse
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid_result_resource import PatchAdSetCategoryBidResultResource
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier import PatchAdSetDisplayMultiplier
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier_list_request import PatchAdSetDisplayMultiplierListRequest
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier_resource import PatchAdSetDisplayMultiplierResource
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier_result_list_response import PatchAdSetDisplayMultiplierResultListResponse
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier_result_resource import PatchAdSetDisplayMultiplierResultResource
from criteo_api_marketingsolutions_preview.model.patch_ad_set_scheduling import PatchAdSetScheduling
from criteo_api_marketingsolutions_preview.model.patch_campaign import PatchCampaign
from criteo_api_marketingsolutions_preview.model.patch_campaign_list_request import PatchCampaignListRequest
from criteo_api_marketingsolutions_preview.model.patch_campaign_spend_limit import PatchCampaignSpendLimit
from criteo_api_marketingsolutions_preview.model.patch_campaign_write_resource import PatchCampaignWriteResource
from criteo_api_marketingsolutions_preview.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from criteo_api_marketingsolutions_preview.model.patch_result_campaign_read_resource import PatchResultCampaignReadResource
from criteo_api_marketingsolutions_preview.model.placements_report_query_data_message import PlacementsReportQueryDataMessage
from criteo_api_marketingsolutions_preview.model.placements_report_query_entity_message import PlacementsReportQueryEntityMessage
from criteo_api_marketingsolutions_preview.model.placements_report_query_message import PlacementsReportQueryMessage
from criteo_api_marketingsolutions_preview.model.portfolio_message import PortfolioMessage
from criteo_api_marketingsolutions_preview.model.preview_error import PreviewError
from criteo_api_marketingsolutions_preview.model.preview_fail_response import PreviewFailResponse
from criteo_api_marketingsolutions_preview.model.preview_warning import PreviewWarning
from criteo_api_marketingsolutions_preview.model.price import Price
from criteo_api_marketingsolutions_preview.model.problem_details import ProblemDetails
from criteo_api_marketingsolutions_preview.model.product import Product
from criteo_api_marketingsolutions_preview.model.product_importer_error import ProductImporterError
from criteo_api_marketingsolutions_preview.model.product_importer_warning import ProductImporterWarning
from criteo_api_marketingsolutions_preview.model.product_set import ProductSet
from criteo_api_marketingsolutions_preview.model.product_set_preview import ProductSetPreview
from criteo_api_marketingsolutions_preview.model.product_set_rule import ProductSetRule
from criteo_api_marketingsolutions_preview.model.product_set_statistics import ProductSetStatistics
from criteo_api_marketingsolutions_preview.model.product_set_statistics_query import ProductSetStatisticsQuery
from criteo_api_marketingsolutions_preview.model.product_shipping import ProductShipping
from criteo_api_marketingsolutions_preview.model.product_shipping_dimension import ProductShippingDimension
from criteo_api_marketingsolutions_preview.model.product_shipping_weight import ProductShippingWeight
from criteo_api_marketingsolutions_preview.model.product_tax import ProductTax
from criteo_api_marketingsolutions_preview.model.product_unit_pricing_base_measure import ProductUnitPricingBaseMeasure
from criteo_api_marketingsolutions_preview.model.product_unit_pricing_measure import ProductUnitPricingMeasure
from criteo_api_marketingsolutions_preview.model.products_custom_batch_request import ProductsCustomBatchRequest
from criteo_api_marketingsolutions_preview.model.products_custom_batch_request_entry import ProductsCustomBatchRequestEntry
from criteo_api_marketingsolutions_preview.model.read_ad_set import ReadAdSet
from criteo_api_marketingsolutions_preview.model.read_ad_set_bidding import ReadAdSetBidding
from criteo_api_marketingsolutions_preview.model.read_ad_set_budget import ReadAdSetBudget
from criteo_api_marketingsolutions_preview.model.read_ad_set_schedule import ReadAdSetSchedule
from criteo_api_marketingsolutions_preview.model.read_model_ad_set_id import ReadModelAdSetId
from criteo_api_marketingsolutions_preview.model.read_model_read_ad_set import ReadModelReadAdSet
from criteo_api_marketingsolutions_preview.model.recommended_product import RecommendedProduct
from criteo_api_marketingsolutions_preview.model.replace_audience import ReplaceAudience
from criteo_api_marketingsolutions_preview.model.replace_audience_request import ReplaceAudienceRequest
from criteo_api_marketingsolutions_preview.model.replace_audience_response import ReplaceAudienceResponse
from criteo_api_marketingsolutions_preview.model.report_data_message import ReportDataMessage
from criteo_api_marketingsolutions_preview.model.report_detail_error import ReportDetailError
from criteo_api_marketingsolutions_preview.model.report_detail_errors import ReportDetailErrors
from criteo_api_marketingsolutions_preview.model.report_entity_message import ReportEntityMessage
from criteo_api_marketingsolutions_preview.model.report_ok_response import ReportOkResponse
from criteo_api_marketingsolutions_preview.model.request_ad_set_search import RequestAdSetSearch
from criteo_api_marketingsolutions_preview.model.requests_ad_set_id import RequestsAdSetId
from criteo_api_marketingsolutions_preview.model.requests_patch_ad_set import RequestsPatchAdSet
from criteo_api_marketingsolutions_preview.model.resource_collection_outcome_of_product_set import ResourceCollectionOutcomeOfProductSet
from criteo_api_marketingsolutions_preview.model.resource_of_product_set import ResourceOfProductSet
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_product_set import ResourceOutcomeOfProductSet
from criteo_api_marketingsolutions_preview.model.response_ad_set_id import ResponseAdSetId
from criteo_api_marketingsolutions_preview.model.response_read_ad_set import ResponseReadAdSet
from criteo_api_marketingsolutions_preview.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_preview.model.responses_read_ad_set import ResponsesReadAdSet
from criteo_api_marketingsolutions_preview.model.rules import Rules
from criteo_api_marketingsolutions_preview.model.size import Size
from criteo_api_marketingsolutions_preview.model.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_api_marketingsolutions_preview.model.tag import Tag
from criteo_api_marketingsolutions_preview.model.target import Target
from criteo_api_marketingsolutions_preview.model.target_type import TargetType
from criteo_api_marketingsolutions_preview.model.targeting_entity import TargetingEntity
from criteo_api_marketingsolutions_preview.model.targeting_error_model import TargetingErrorModel
from criteo_api_marketingsolutions_preview.model.targeting_operator import TargetingOperator
from criteo_api_marketingsolutions_preview.model.third_party_html_attributes import ThirdPartyHtmlAttributes
from criteo_api_marketingsolutions_preview.model.third_party_html_write_attributes import ThirdPartyHtmlWriteAttributes
from criteo_api_marketingsolutions_preview.model.transactions_report_query_data_message import TransactionsReportQueryDataMessage
from criteo_api_marketingsolutions_preview.model.transactions_report_query_entity_message import TransactionsReportQueryEntityMessage
from criteo_api_marketingsolutions_preview.model.transactions_report_query_message import TransactionsReportQueryMessage
from criteo_api_marketingsolutions_preview.model.transparency_query_message import TransparencyQueryMessage
from criteo_api_marketingsolutions_preview.model.transparency_report_attributes import TransparencyReportAttributes
from criteo_api_marketingsolutions_preview.model.transparency_report_data_message import TransparencyReportDataMessage
from criteo_api_marketingsolutions_preview.model.transparency_report_entity_message import TransparencyReportEntityMessage
from criteo_api_marketingsolutions_preview.model.transparency_report_file import TransparencyReportFile
from criteo_api_marketingsolutions_preview.model.unauthorized_response_v2 import UnauthorizedResponseV2
from criteo_api_marketingsolutions_preview.model.update_coupon import UpdateCoupon
from criteo_api_marketingsolutions_preview.model.update_coupon_request import UpdateCouponRequest
from criteo_api_marketingsolutions_preview.model.update_coupon_resource import UpdateCouponResource
from criteo_api_marketingsolutions_preview.model.user_def import UserDef
from criteo_api_marketingsolutions_preview.model.user_event import UserEvent
from criteo_api_marketingsolutions_preview.model.value_resource_input_of_create_product_set_request import ValueResourceInputOfCreateProductSetRequest
from criteo_api_marketingsolutions_preview.model.value_resource_of_create_product_set_request import ValueResourceOfCreateProductSetRequest
from criteo_api_marketingsolutions_preview.model.write_model_ad_set_id import WriteModelAdSetId
from criteo_api_marketingsolutions_preview.model.write_model_patch_ad_set import WriteModelPatchAdSet
