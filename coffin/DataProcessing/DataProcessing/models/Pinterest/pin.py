# generated by datamodel-codegen:
#   filename:  data2.json
#   timestamp: 2024-11-10T19:45:19+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class OriginPinner(BaseModel):
    node_id: Optional[str] = None
    first_name: Optional[str] = None
    image_small_url: Optional[str] = None
    type: Optional[str] = None
    is_verified_merchant: Optional[bool] = None
    explicitly_followed_by_me: Optional[bool] = None
    full_name: Optional[str] = None
    blocked_by_me: Optional[bool] = None
    verified_identity: Optional[Dict[str, Any]] = None
    indexed: Optional[bool] = None
    domain_url: Optional[Any] = None
    domain_verified: Optional[bool] = None
    id: Optional[str] = None
    image_medium_url: Optional[str] = None
    follower_count: Optional[int] = None
    is_default_image: Optional[bool] = None
    username: Optional[str] = None
    ads_only_profile_site: Optional[Any] = None
    followed_by_me: Optional[bool] = None
    is_ads_only_profile: Optional[bool] = None


class Field60x60(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field136x136(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field170x(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field236x(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field474x(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field564x(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field736x(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Field600x315(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Orig(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class Images(BaseModel):
    field_60x60: Optional[Field60x60] = Field(None, alias='60x60')
    field_136x136: Optional[Field136x136] = Field(None, alias='136x136')
    field_170x: Optional[Field170x] = Field(None, alias='170x')
    field_236x: Optional[Field236x] = Field(None, alias='236x')
    field_474x: Optional[Field474x] = Field(None, alias='474x')
    field_564x: Optional[Field564x] = Field(None, alias='564x')
    field_736x: Optional[Field736x] = Field(None, alias='736x')
    field_600x315: Optional[Field600x315] = Field(None, alias='600x315')
    orig: Optional[Orig] = None


class Owner(BaseModel):
    node_id: Optional[str] = None
    first_name: Optional[str] = None
    image_small_url: Optional[str] = None
    type: Optional[str] = None
    is_verified_merchant: Optional[bool] = None
    explicitly_followed_by_me: Optional[bool] = None
    full_name: Optional[str] = None
    blocked_by_me: Optional[bool] = None
    verified_identity: Optional[Dict[str, Any]] = None
    indexed: Optional[bool] = None
    domain_url: Optional[Any] = None
    domain_verified: Optional[bool] = None
    id: Optional[str] = None
    image_medium_url: Optional[str] = None
    follower_count: Optional[int] = None
    is_default_image: Optional[bool] = None
    username: Optional[str] = None
    ads_only_profile_site: Optional[Any] = None
    followed_by_me: Optional[bool] = None
    is_ads_only_profile: Optional[bool] = None


class Board(BaseModel):
    node_id: Optional[str] = None
    type: Optional[str] = None
    collaborated_by_me: Optional[bool] = None
    is_collaborative: Optional[bool] = None
    category: Optional[Any] = None
    image_cover_url: Optional[str] = None
    name: Optional[str] = None
    privacy: Optional[str] = None
    owner: Optional[Owner] = None
    followed_by_me: Optional[bool] = None
    url: Optional[str] = None
    pin_thumbnail_urls: Optional[List[str]] = None
    description: Optional[str] = None
    map_id: Optional[str] = None
    access: Optional[List] = None
    image_thumbnail_url: Optional[str] = None
    layout: Optional[str] = None
    id: Optional[str] = None


class ViaPinner(BaseModel):
    node_id: Optional[str] = None
    first_name: Optional[str] = None
    image_small_url: Optional[str] = None
    type: Optional[str] = None
    is_verified_merchant: Optional[bool] = None
    explicitly_followed_by_me: Optional[bool] = None
    full_name: Optional[str] = None
    blocked_by_me: Optional[bool] = None
    verified_identity: Optional[Dict[str, Any]] = None
    indexed: Optional[bool] = None
    domain_url: Optional[Any] = None
    domain_verified: Optional[bool] = None
    id: Optional[str] = None
    image_medium_url: Optional[str] = None
    follower_count: Optional[int] = None
    is_default_image: Optional[bool] = None
    username: Optional[str] = None
    ads_only_profile_site: Optional[Any] = None
    followed_by_me: Optional[bool] = None
    is_ads_only_profile: Optional[bool] = None


class Pinner(BaseModel):
    node_id: Optional[str] = None
    first_name: Optional[str] = None
    image_small_url: Optional[str] = None
    type: Optional[str] = None
    is_verified_merchant: Optional[bool] = None
    explicitly_followed_by_me: Optional[bool] = None
    full_name: Optional[str] = None
    blocked_by_me: Optional[bool] = None
    verified_identity: Optional[Dict[str, Any]] = None
    indexed: Optional[bool] = None
    domain_url: Optional[Any] = None
    domain_verified: Optional[bool] = None
    id: Optional[str] = None
    image_medium_url: Optional[str] = None
    follower_count: Optional[int] = None
    is_default_image: Optional[bool] = None
    username: Optional[str] = None
    ads_only_profile_site: Optional[Any] = None
    followed_by_me: Optional[bool] = None
    is_ads_only_profile: Optional[bool] = None


class Originals(BaseModel):
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class Field750x(BaseModel):
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class Field736x1(BaseModel):
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class Images1(BaseModel):
    originals: Optional[Originals] = None
    field_750x: Optional[Field750x] = Field(None, alias='750x')
    field_736x: Optional[Field736x1] = Field(None, alias='736x')


class ImageAdjusted(BaseModel):
    images: Optional[Images1] = None
    dominant_color: Optional[str] = None


class Field236x1(BaseModel):
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class Images2(BaseModel):
    originals: Optional[Originals] = None
    field_236x: Optional[Field236x1] = Field(None, alias='236x')
    field_750x: Optional[Field750x] = Field(None, alias='750x')
    field_736x: Optional[Field736x1] = Field(None, alias='736x')


class Image(BaseModel):
    images: Optional[Images2] = None
    dominant_color: Optional[str] = None


class BlockStyle(BaseModel):
    height: Optional[int] = None
    rotation: Optional[int] = None
    y_coord: Optional[int] = None
    width: Optional[int] = None
    x_coord: Optional[int] = None
    corner_radius: Optional[int] = None


class CaptionsUrls(BaseModel):
    en_za: Optional[str] = Field(None, alias='en-za')


class VEXP5(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    captions_urls: Optional[CaptionsUrls] = None
    best_captions_url: Optional[Any] = None


class VEXP7(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    captions_urls: Optional[CaptionsUrls] = None
    best_captions_url: Optional[Any] = None


class VEXP4(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    captions_urls: Optional[CaptionsUrls] = None
    best_captions_url: Optional[Any] = None


class VEXP6(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    captions_urls: Optional[CaptionsUrls] = None
    best_captions_url: Optional[Any] = None


class VHLSV3MOBILE(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    captions_urls: Optional[CaptionsUrls] = None
    best_captions_url: Optional[Any] = None


class VEXP3(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    captions_urls: Optional[CaptionsUrls] = None
    best_captions_url: Optional[Any] = None


class VideoList(BaseModel):
    V_EXP5: Optional[VEXP5] = None
    V_EXP7: Optional[VEXP7] = None
    V_EXP4: Optional[VEXP4] = None
    V_EXP6: Optional[VEXP6] = None
    V_HLSV3_MOBILE: Optional[VHLSV3MOBILE] = None
    V_EXP3: Optional[VEXP3] = None


class Video(BaseModel):
    video_list: Optional[VideoList] = None
    id: Optional[str] = None
    bitrates: Optional[Any] = None


class Block(BaseModel):
    type: Optional[str] = None
    block_style: Optional[BlockStyle] = None
    video_signature: Optional[str] = None
    video: Optional[Video] = None
    block_type: Optional[int] = None


class Page(BaseModel):
    image_signature: Optional[str] = None
    type: Optional[str] = None
    layout: Optional[int] = None
    video_signature: Optional[Any] = None
    image_adjusted: Optional[ImageAdjusted] = None
    should_mute: Optional[bool] = None
    image: Optional[Image] = None
    blocks: Optional[List[Block]] = None
    music_attributions: Optional[List] = None
    video: Optional[Any] = None
    image_signature_adjusted: Optional[str] = None
    id: Optional[str] = None


class Basics(BaseModel):
    key_value_blocks: Optional[List] = None
    list_blocks: Optional[List] = None


class Metadata(BaseModel):
    pin_title: Optional[str] = None
    canvas_aspect_ratio: Optional[float] = None
    root_user_id: Optional[str] = None
    is_compatible: Optional[bool] = None
    version: Optional[str] = None
    pin_image_signature: Optional[str] = None
    compatible_version: Optional[str] = None
    showreel_data: Optional[Any] = None
    basics: Optional[Basics] = None
    is_promotable: Optional[bool] = None
    template_type: Optional[Any] = None
    is_editable: Optional[bool] = None
    root_pin_id: Optional[str] = None
    diy_data: Optional[Any] = None
    recipe_data: Optional[Any] = None


class StoryPinData(BaseModel):
    node_id: Optional[str] = None
    type: Optional[str] = None
    pages: Optional[List[Page]] = None
    is_deleted: Optional[bool] = None
    page_count: Optional[int] = None
    mentioned_users: Optional[List] = None
    metadata: Optional[Metadata] = None
    has_affiliate_products: Optional[bool] = None
    has_product_pins: Optional[bool] = None
    last_edited: Optional[Any] = None
    id: Optional[str] = None


class CloseupAttribution(BaseModel):
    node_id: Optional[str] = None
    first_name: Optional[str] = None
    image_small_url: Optional[str] = None
    type: Optional[str] = None
    is_verified_merchant: Optional[bool] = None
    explicitly_followed_by_me: Optional[bool] = None
    full_name: Optional[str] = None
    blocked_by_me: Optional[bool] = None
    verified_identity: Optional[Dict[str, Any]] = None
    indexed: Optional[bool] = None
    domain_url: Optional[Any] = None
    domain_verified: Optional[bool] = None
    id: Optional[str] = None
    image_medium_url: Optional[str] = None
    follower_count: Optional[int] = None
    is_default_image: Optional[bool] = None
    username: Optional[str] = None
    ads_only_profile_site: Optional[Any] = None
    followed_by_me: Optional[bool] = None
    is_ads_only_profile: Optional[bool] = None


class ReactionCounts(BaseModel):
    field_1: Optional[int] = Field(None, alias='1')
    field_11: Optional[int] = Field(None, alias='11')
    field_13: Optional[int] = Field(None, alias='13')


class AggregatedStats(BaseModel):
    saves: Optional[int] = None
    done: Optional[int] = None


class RecommendScore(BaseModel):
    score: Optional[float] = None
    count: Optional[int] = None


class DidItData(BaseModel):
    type: Optional[str] = None
    responses_count: Optional[int] = None
    recommended_count: Optional[int] = None
    recommend_scores: Optional[List[RecommendScore]] = None
    videos_count: Optional[int] = None
    images_count: Optional[int] = None
    rating: Optional[int] = None
    tags: Optional[List] = None
    details_count: Optional[int] = None
    user_count: Optional[int] = None


class AggregatedPinData(BaseModel):
    node_id: Optional[str] = None
    aggregated_stats: Optional[AggregatedStats] = None
    did_it_data: Optional[DidItData] = None
    comment_count: Optional[int] = None
    id: Optional[str] = None
    is_shop_the_look: Optional[bool] = None


class CanonicalPin(BaseModel):
    id: Optional[str] = None


class HowLifeFeelsWhen(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class VideoForStoryInstagram(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class InAnotherLifeAesthetic(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class AestheticLovePictures(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class CoolVideosAesthetic(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class AestheticPostForInstagram(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class InstagramVideoStoryIdeas(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class CuteVideoEditsAesthetic(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class LoveFeelingVideo(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


class AnnotationsWithLinks(BaseModel):
    How_Life_Feels_When: Optional[HowLifeFeelsWhen] = Field(
        None, alias='How Life Feels When'
    )
    Video_For_Story_Instagram: Optional[VideoForStoryInstagram] = Field(
        None, alias='Video For Story Instagram'
    )
    In_Another_Life_Aesthetic: Optional[InAnotherLifeAesthetic] = Field(
        None, alias='In Another Life Aesthetic'
    )
    Aesthetic_Love_Pictures: Optional[AestheticLovePictures] = Field(
        None, alias='Aesthetic Love Pictures'
    )
    Cool_Videos_Aesthetic: Optional[CoolVideosAesthetic] = Field(
        None, alias='Cool Videos Aesthetic'
    )
    Aesthetic_Post_For_Instagram: Optional[AestheticPostForInstagram] = Field(
        None, alias='Aesthetic Post For Instagram'
    )
    Instagram_Video_Story_Ideas: Optional[InstagramVideoStoryIdeas] = Field(
        None, alias='Instagram Video Story Ideas'
    )
    Cute_Video_Edits_Aesthetic: Optional[CuteVideoEditsAesthetic] = Field(
        None, alias='Cute Video Edits Aesthetic'
    )
    Love_Feeling_Video: Optional[LoveFeelingVideo] = Field(
        None, alias='Love Feeling Video'
    )


class SeoBreadcrumb(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


class PinJoin(BaseModel):
    visual_annotation: Optional[List[str]] = None
    seo_canonical_domain: Optional[str] = None
    seo_canonical_url: Optional[str] = None
    canonical_pin: Optional[CanonicalPin] = None
    annotations_with_links: Optional[AnnotationsWithLinks] = None
    shopping_klp_urls: Optional[Any] = None
    seo_breadcrumbs: Optional[List[SeoBreadcrumb]] = None


class NativeCreator(BaseModel):
    node_id: Optional[str] = None
    first_name: Optional[str] = None
    image_small_url: Optional[str] = None
    type: Optional[str] = None
    is_verified_merchant: Optional[bool] = None
    explicitly_followed_by_me: Optional[bool] = None
    full_name: Optional[str] = None
    blocked_by_me: Optional[bool] = None
    verified_identity: Optional[Dict[str, Any]] = None
    indexed: Optional[bool] = None
    domain_url: Optional[Any] = None
    domain_verified: Optional[bool] = None
    id: Optional[str] = None
    image_medium_url: Optional[str] = None
    follower_count: Optional[int] = None
    is_default_image: Optional[bool] = None
    username: Optional[str] = None
    ads_only_profile_site: Optional[Any] = None
    followed_by_me: Optional[bool] = None
    is_ads_only_profile: Optional[bool] = None


class CarouselSlot(BaseModel):
    images: Optional[Images] = None
    title: Optional[str] = None
    details: Optional[str] = None
    id: Optional[str] = None
    domain: Optional[str] = None
    link: Optional[str] = None


class CarouselData(BaseModel):
    node_id: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None
    carousel_slots: Optional[List[CarouselSlot]] = None
    rich_metadata: Optional[List] = None
    rich_summary: Optional[List] = None
    index: Optional[int] = None



class Data(BaseModel):
    node_id: Optional[str] = None
    alt_text: Optional[Any] = None
    origin_pinner: Optional[OriginPinner] = None
    images: Optional[Images] = None
    promoter: Optional[Any] = None
    embed: Optional[Any] = None
    closeup_unified_description: Optional[str] = None
    is_v1_idea_pin: Optional[bool] = None
    board: Optional[Board] = None
    via_pinner: Optional[ViaPinner] = None
    content_sensitivity: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    dominant_color: Optional[str] = None
    shuffle: Optional[Any] = None
    domain: Optional[str] = None
    id: Optional[str] = None
    is_video: Optional[bool] = None
    collection_pin: Optional[Any] = None
    is_quick_promotable_by_pinner: Optional[bool] = None
    pinner: Optional[Pinner] = None
    music_attributions: Optional[List] = None
    description: Optional[str] = None
    method: Optional[str] = None
    tracked_link: Optional[Any] = None
    closeup_description: Optional[Any] = None
    rich_metadata: Optional[Any] = None
    tracking_params: Optional[str] = None
    comments_disabled: Optional[bool] = None
    privacy: Optional[str] = None
    story_pin_data: Optional[StoryPinData] = None
    closeup_attribution: Optional[CloseupAttribution] = None
    reaction_counts: Optional[ReactionCounts] = None
    description_html: Optional[str] = None
    repin_count: Optional[int] = None
    media_attribution: Optional[Any] = None
    link_domain: Optional[Any] = None
    story_pin_data_id: Optional[str] = None
    is_repin: Optional[bool] = None
    seo_description: Optional[str] = None
    is_eligible_for_brand_catalog: Optional[bool] = None
    is_playable: Optional[bool] = None
    is_native: Optional[bool] = None
    seo_title: Optional[str] = None
    price_value: Optional[int] = None
    third_party_pin_owner: Optional[Any] = None
    title: Optional[str] = None
    hashtags: Optional[List[str]] = None
    should_open_in_stream: Optional[bool] = None
    access: Optional[List] = None
    attribution: Optional[Any] = None
    pinned_to_board: Optional[Any] = None
    is_stale_product: Optional[bool] = None
    related_article: Optional[Dict[str, Any]] = None
    formatted_description: Optional[Dict[str, Any]] = None
    share_count: Optional[int] = None
    category: Optional[str] = None
    mobile_link: Optional[Any] = None
    is_eligible_for_pdp: Optional[bool] = None
    product_pin_data: Optional[Any] = None
    link: Optional[Any] = None
    grid_title: Optional[str] = None
    is_whitelisted_for_tried_it: Optional[bool] = None
    is_quick_promotable: Optional[bool] = None
    buyable_product_availability: Optional[Any] = None
    digital_media_source_type: Optional[Any] = None
    closeup_user_note: Optional[str] = None
    is_hidden: Optional[bool] = None
    did_it_disabled: Optional[bool] = None
    price_currency: Optional[str] = None
    is_oos_product: Optional[bool] = None
    seo_noindex_reason: Optional[Any] = None
    sponsorship: Optional[Any] = None
    creator_class_instance: Optional[Any] = None
    promoted_is_removable: Optional[bool] = None
    is_eligible_for_aggregated_comments: Optional[bool] = None
    can_delete_did_it_and_comments: Optional[bool] = None
    shopping_flags: Optional[List] = None
    should_mute: Optional[bool] = None
    shopping_rec_disabled: Optional[bool] = None
    is_promotable: Optional[bool] = None
    comment_count: Optional[int] = None
    creator_class: Optional[Any] = None
    videos: Optional[Any] = None
    seo_url: Optional[str] = None
    aggregated_pin_data: Optional[AggregatedPinData] = None
    image_signature: Optional[str] = None
    type: Optional[str] = None
    should_redirect_id_only_url_to_text_url: Optional[bool] = None
    carousel_data: Optional[CarouselData] = None
    pin_join: Optional[PinJoin] = None
    auto_alt_text: Optional[str] = None
    image_medium_url: Optional[str] = None
    native_creator: Optional[NativeCreator] = None
    section: Optional[Any] = None
    is_promoted: Optional[bool] = None


class ResourceResponse(BaseModel):
    status: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None
    endpoint_name: Optional[str] = None
    data: Optional[Data] = None
    x_pinterest_sli_endpoint_name: Optional[str] = None
    http_status: Optional[int] = None


class AnalysisUa(BaseModel):
    app_type: Optional[int] = None
    browser_name: Optional[str] = None
    browser_version: Optional[str] = None
    device_type: Optional[Any] = None
    device: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None


class User(BaseModel):
    unauth_id: Optional[str] = None
    ip_country: Optional[str] = None
    ip_region: Optional[str] = None


class ClientContext(BaseModel):
    analysis_ua: Optional[AnalysisUa] = None
    app_type_detailed: Optional[int] = None
    app_version: Optional[str] = None
    batch_exp: Optional[bool] = None
    browser_locale: Optional[str] = None
    browser_name: Optional[str] = None
    browser_type: Optional[int] = None
    browser_version: Optional[str] = None
    country: Optional[str] = None
    country_from_hostname: Optional[str] = None
    country_from_ip: Optional[str] = None
    csp_nonce: Optional[str] = None
    current_url: Optional[str] = None
    debug: Optional[bool] = None
    deep_link: Optional[str] = None
    enabled_advertiser_countries: Optional[List[str]] = None
    facebook_token: Optional[Any] = None
    full_path: Optional[str] = None
    http_referrer: Optional[str] = None
    impersonator_user_id: Optional[Any] = None
    invite_code: Optional[str] = None
    invite_sender_id: Optional[str] = None
    is_authenticated: Optional[bool] = None
    is_bot: Optional[str] = None
    is_internal_ip: Optional[bool] = None
    is_full_page: Optional[bool] = None
    is_mobile_agent: Optional[bool] = None
    is_sterling_on_steroids: Optional[bool] = None
    is_tablet_agent: Optional[bool] = None
    language: Optional[str] = None
    locale: Optional[str] = None
    origin: Optional[str] = None
    path: Optional[str] = None
    placed_experiences: Optional[Any] = None
    referrer: Optional[Any] = None
    region_from_ip: Optional[str] = None
    request_host: Optional[str] = None
    request_identifier: Optional[str] = None
    social_bot: Optional[str] = None
    stage: Optional[str] = None
    sterling_on_steroids_ldap: Optional[Any] = None
    sterling_on_steroids_user_type: Optional[Any] = None
    theme: Optional[str] = None
    unauth_id: Optional[str] = None
    seo_debug: Optional[bool] = None
    user_agent_can_use_native_app: Optional[bool] = None
    user_agent_platform: Optional[str] = None
    user_agent_platform_version: Optional[Any] = None
    user_agent: Optional[str] = None
    user: Optional[User] = None
    utm_campaign: Optional[Any] = None
    visible_url: Optional[str] = None


class Options(BaseModel):
    bookmarks: Optional[List[str]] = None
    field_set_key: Optional[str] = None
    id: Optional[str] = None


class Resource(BaseModel):
    name: Optional[str] = None
    options: Optional[Options] = None


class PinterestPinResponse(BaseModel):
    resource_response: Optional[ResourceResponse] = None
    client_context: Optional[ClientContext] = None
    resource: Optional[Resource] = None
    request_identifier: Optional[str] = None