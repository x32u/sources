# generated by datamodel-codegen:
#   filename:  feed.json
#   timestamp: 2024-06-19T00:01:40+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, RootModel # type: ignore


class Author(BaseModel):
    avatarLarger: Optional[str] = None
    avatarMedium: Optional[str] = None
    avatarThumb: Optional[str] = None
    commentSetting: Optional[int] = None
    downloadSetting: Optional[int] = None
    duetSetting: Optional[int] = None
    ftc: Optional[bool] = None
    id: Optional[str] = None
    isADVirtual: Optional[bool] = None
    isEmbedBanned: Optional[bool] = None
    nickname: Optional[str] = None
    openFavorite: Optional[bool] = None
    privateAccount: Optional[bool] = None
    relation: Optional[int] = None
    secUid: Optional[str] = None
    secret: Optional[bool] = None
    signature: Optional[str] = None
    stitchSetting: Optional[int] = None
    uniqueId: Optional[str] = None
    verified: Optional[bool] = None


class Content(BaseModel):
    desc: Optional[str] = None


class ItemControl(BaseModel):
    can_repost: Optional[bool] = None


class Music(BaseModel):
    album: Optional[str] = None
    authorName: Optional[str] = None
    coverLarge: Optional[str] = None
    coverMedium: Optional[str] = None
    coverThumb: Optional[str] = None
    duration: Optional[int] = None
    id: Optional[str] = None
    original: Optional[bool] = None
    playUrl: Optional[str] = None
    title: Optional[str] = None


class Stats(BaseModel):
    collectCount: Optional[int] = None
    commentCount: Optional[int] = None
    diggCount: Optional[int] = None
    playCount: Optional[int] = None
    shareCount: Optional[int] = None


class StatsV2(BaseModel):
    collectCount: Optional[str] = None
    commentCount: Optional[str] = None
    diggCount: Optional[str] = None
    playCount: Optional[str] = None
    repostCount: Optional[str] = None
    shareCount: Optional[str] = None


class PlayAddr(BaseModel):
    DataSize: Optional[int] = None
    FileCs: Optional[str] = None
    FileHash: Optional[str] = None
    Uri: Optional[str] = None
    UrlKey: Optional[str] = None
    UrlList: Optional[List[str]] = None


class BitrateInfoItem(BaseModel):
    Bitrate: Optional[int] = None
    CodecType: Optional[str] = None
    GearName: Optional[str] = None
    PlayAddr: Optional[PlayAddr] = None
    QualityType: Optional[int] = None


class VolumeInfo(BaseModel):
    Loudness: Optional[float] = None
    Peak: Optional[float] = None


class ZoomCover(BaseModel):
    field_240: Optional[str] = Field(None, alias='240')
    field_480: Optional[str] = Field(None, alias='480')
    field_720: Optional[str] = Field(None, alias='720')
    field_960: Optional[str] = Field(None, alias='960')


class SubtitleInfo(BaseModel):
    Format: Optional[str] = None
    LanguageCodeName: Optional[str] = None
    LanguageID: Optional[str] = None
    Size: Optional[int] = None
    Source: Optional[str] = None
    Url: Optional[str] = None
    UrlExpire: Optional[int] = None
    Version: Optional[str] = None


class Video(BaseModel):
    bitrate: Optional[int] = None
    bitrateInfo: Optional[List[BitrateInfoItem]] = None
    codecType: Optional[str] = None
    cover: Optional[str] = None
    definition: Optional[str] = None
    downloadAddr: Optional[str] = None
    duration: Optional[int] = None
    dynamicCover: Optional[str] = None
    encodeUserTag: Optional[str] = None
    encodedType: Optional[str] = None
    format: Optional[str] = None
    height: Optional[int] = None
    id: Optional[str] = None
    originCover: Optional[str] = None
    playAddr: Optional[str] = None
    ratio: Optional[str] = None
    videoQuality: Optional[str] = None
    volumeInfo: Optional[VolumeInfo] = None
    width: Optional[int] = None
    zoomCover: Optional[ZoomCover] = None
    subtitleInfos: Optional[List[SubtitleInfo]] = None


class ImageURL(BaseModel):
    urlList: Optional[List[str]] = None


class Cover(BaseModel):
    imageHeight: Optional[int] = None
    imageURL: Optional[ImageURL] = None
    imageWidth: Optional[int] = None


class Image(BaseModel):
    imageHeight: Optional[int] = None
    imageURL: Optional[ImageURL] = None
    imageWidth: Optional[int] = None


class ShareCover(BaseModel):
    imageHeight: Optional[int] = None
    imageURL: Optional[ImageURL] = None
    imageWidth: Optional[int] = None


class ImagePost(BaseModel):
    cover: Optional[Cover] = None
    images: Optional[List[Image]] = None
    shareCover: Optional[ShareCover] = None
    title: Optional[str] = None


class ExtraInfo(BaseModel):
    subtype: Optional[str] = None


class Icon(BaseModel):
    urlList: Optional[List[str]] = None


class Thumbnail(BaseModel):
    height: Optional[int] = None
    urlList: Optional[List[str]] = None
    width: Optional[int] = None


class Anchor(BaseModel):
    description: Optional[str] = None
    extraInfo: Optional[ExtraInfo] = None
    icon: Optional[Icon] = None
    id: Optional[str] = None
    keyword: Optional[str] = None
    logExtra: Optional[str] = None
    schema_: Optional[str] = Field(None, alias='schema')
    thumbnail: Optional[Thumbnail] = None
    type: Optional[int] = None


class Word(BaseModel):
    word: Optional[str] = None
    word_id: Optional[str] = None


class VideoSuggestWordsStructItem(BaseModel):
    hint_text: Optional[str] = None
    scene: Optional[str] = None
    words: Optional[List[Word]] = None


class VideoSuggestWordsList(BaseModel):
    video_suggest_words_struct: Optional[List[VideoSuggestWordsStructItem]] = None


class UserFeedItem(BaseModel):
    AIGCDescription: Optional[str] = None
    author: Optional[Author] = None
    collected: Optional[bool] = None
    contents: Optional[List[Content]] = None
    createTime: Optional[int] = None
    desc: Optional[str] = None
    digged: Optional[bool] = None
    diversificationId: Optional[int] = None
    duetDisplay: Optional[int] = None
    duetEnabled: Optional[bool] = None
    forFriend: Optional[bool] = None
    id: Optional[str] = None
    itemCommentStatus: Optional[int] = None
    item_control: Optional[ItemControl] = None
    music: Optional[Music] = None
    officalItem: Optional[bool] = None
    originalItem: Optional[bool] = None
    privateItem: Optional[bool] = None
    secret: Optional[bool] = None
    shareEnabled: Optional[bool] = None
    stats: Optional[Stats] = None
    statsV2: Optional[StatsV2] = None
    stitchDisplay: Optional[int] = None
    stitchEnabled: Optional[bool] = None
    video: Optional[Video] = None
    imagePost: Optional[ImagePost] = None
    anchors: Optional[List[Anchor]] = None
    videoSuggestWordsList: Optional[VideoSuggestWordsList] = None


class UserFeed(RootModel):
    root: Optional[List[UserFeedItem]] = None