# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .RhoTypes_pb2 import (
    BindPattern as RhoTypes_pb2___BindPattern,
    Par as RhoTypes_pb2___Par,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class FindDeployQuery(google___protobuf___message___Message):
    deployId = ... # type: bytes

    def __init__(self,
        *,
        deployId : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FindDeployQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"deployId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"deployId",b"deployId"]) -> None: ...

class BlockQuery(google___protobuf___message___Message):
    hash = ... # type: typing___Text

    def __init__(self,
        *,
        hash : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",b"hash"]) -> None: ...

class BlocksQuery(google___protobuf___message___Message):
    depth = ... # type: int

    def __init__(self,
        *,
        depth : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlocksQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"depth"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",b"depth"]) -> None: ...

class DataAtNameQuery(google___protobuf___message___Message):
    depth = ... # type: int

    @property
    def name(self) -> RhoTypes_pb2___Par: ...

    def __init__(self,
        *,
        depth : typing___Optional[int] = None,
        name : typing___Optional[RhoTypes_pb2___Par] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DataAtNameQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",u"name"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",b"depth",u"name",b"name"]) -> None: ...

class ContinuationAtNameQuery(google___protobuf___message___Message):
    depth = ... # type: int

    @property
    def names(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RhoTypes_pb2___Par]: ...

    def __init__(self,
        *,
        depth : typing___Optional[int] = None,
        names : typing___Optional[typing___Iterable[RhoTypes_pb2___Par]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ContinuationAtNameQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",u"names"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",b"depth",u"names",b"names"]) -> None: ...

class DeployServiceResponse(google___protobuf___message___Message):
    message = ... # type: typing___Text

    def __init__(self,
        *,
        message : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeployServiceResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"message"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"message",b"message"]) -> None: ...

class BlockQueryResponse(google___protobuf___message___Message):

    @property
    def blockInfo(self) -> BlockInfo: ...

    def __init__(self,
        *,
        blockInfo : typing___Optional[BlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockQueryResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo"]) -> None: ...

class LightBlockQueryResponse(google___protobuf___message___Message):

    @property
    def blockInfo(self) -> LightBlockInfo: ...

    def __init__(self,
        *,
        blockInfo : typing___Optional[LightBlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LightBlockQueryResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo"]) -> None: ...

class VisualizeDagQuery(google___protobuf___message___Message):
    depth = ... # type: int
    showJustificationLines = ... # type: bool

    def __init__(self,
        *,
        depth : typing___Optional[int] = None,
        showJustificationLines : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VisualizeDagQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",u"showJustificationLines"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"depth",b"depth",u"showJustificationLines",b"showJustificationLines"]) -> None: ...

class VisualizeBlocksResponse(google___protobuf___message___Message):
    content = ... # type: typing___Text

    def __init__(self,
        *,
        content : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VisualizeBlocksResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"content"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content"]) -> None: ...

class MachineVerifyQuery(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MachineVerifyQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class MachineVerifyResponse(google___protobuf___message___Message):
    content = ... # type: typing___Text

    def __init__(self,
        *,
        content : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MachineVerifyResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"content"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content"]) -> None: ...

class ListeningNameDataResponse(google___protobuf___message___Message):
    length = ... # type: int

    @property
    def blockResults(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DataWithBlockInfo]: ...

    def __init__(self,
        *,
        blockResults : typing___Optional[typing___Iterable[DataWithBlockInfo]] = None,
        length : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListeningNameDataResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockResults",u"length"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockResults",b"blockResults",u"length",b"length"]) -> None: ...

class ListeningNameContinuationResponse(google___protobuf___message___Message):
    length = ... # type: int

    @property
    def blockResults(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ContinuationsWithBlockInfo]: ...

    def __init__(self,
        *,
        blockResults : typing___Optional[typing___Iterable[ContinuationsWithBlockInfo]] = None,
        length : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListeningNameContinuationResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockResults",u"length"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockResults",b"blockResults",u"length",b"length"]) -> None: ...

class PrivateNamePreviewQuery(google___protobuf___message___Message):
    user = ... # type: bytes
    timestamp = ... # type: int
    nameQty = ... # type: int

    def __init__(self,
        *,
        user : typing___Optional[bytes] = None,
        timestamp : typing___Optional[int] = None,
        nameQty : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrivateNamePreviewQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"nameQty",u"timestamp",u"user"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"nameQty",b"nameQty",u"timestamp",b"timestamp",u"user",b"user"]) -> None: ...

class PrivateNamePreviewResponse(google___protobuf___message___Message):
    ids = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]

    def __init__(self,
        *,
        ids : typing___Optional[typing___Iterable[bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrivateNamePreviewResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"ids"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids"]) -> None: ...

class LastFinalizedBlockQuery(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LastFinalizedBlockQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class LastFinalizedBlockResponse(google___protobuf___message___Message):

    @property
    def blockInfo(self) -> BlockInfo: ...

    def __init__(self,
        *,
        blockInfo : typing___Optional[BlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LastFinalizedBlockResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo"]) -> None: ...

class IsFinalizedQuery(google___protobuf___message___Message):
    hash = ... # type: typing___Text

    def __init__(self,
        *,
        hash : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> IsFinalizedQuery: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",b"hash"]) -> None: ...

class IsFinalizedResponse(google___protobuf___message___Message):
    isFinalized = ... # type: bool

    def __init__(self,
        *,
        isFinalized : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> IsFinalizedResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"isFinalized"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"isFinalized",b"isFinalized"]) -> None: ...

class LightBlockInfo(google___protobuf___message___Message):
    blockHash = ... # type: typing___Text
    blockSize = ... # type: typing___Text
    blockNumber = ... # type: int
    version = ... # type: int
    deployCount = ... # type: int
    tupleSpaceHash = ... # type: typing___Text
    timestamp = ... # type: int
    faultTolerance = ... # type: float
    mainParentHash = ... # type: typing___Text
    parentsHashList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    sender = ... # type: typing___Text

    def __init__(self,
        *,
        blockHash : typing___Optional[typing___Text] = None,
        blockSize : typing___Optional[typing___Text] = None,
        blockNumber : typing___Optional[int] = None,
        version : typing___Optional[int] = None,
        deployCount : typing___Optional[int] = None,
        tupleSpaceHash : typing___Optional[typing___Text] = None,
        timestamp : typing___Optional[int] = None,
        faultTolerance : typing___Optional[float] = None,
        mainParentHash : typing___Optional[typing___Text] = None,
        parentsHashList : typing___Optional[typing___Iterable[typing___Text]] = None,
        sender : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LightBlockInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",u"blockNumber",u"blockSize",u"deployCount",u"faultTolerance",u"mainParentHash",u"parentsHashList",u"sender",u"timestamp",u"tupleSpaceHash",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",b"blockHash",u"blockNumber",b"blockNumber",u"blockSize",b"blockSize",u"deployCount",b"deployCount",u"faultTolerance",b"faultTolerance",u"mainParentHash",b"mainParentHash",u"parentsHashList",b"parentsHashList",u"sender",b"sender",u"timestamp",b"timestamp",u"tupleSpaceHash",b"tupleSpaceHash",u"version",b"version"]) -> None: ...

class BlockInfo(google___protobuf___message___Message):
    blockHash = ... # type: typing___Text
    blockSize = ... # type: typing___Text
    blockNumber = ... # type: int
    version = ... # type: int
    deployCount = ... # type: int
    tupleSpaceHash = ... # type: typing___Text
    timestamp = ... # type: int
    faultTolerance = ... # type: float
    mainParentHash = ... # type: typing___Text
    parentsHashList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    sender = ... # type: typing___Text
    shardId = ... # type: typing___Text
    bondsValidatorList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    deployCost = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        blockHash : typing___Optional[typing___Text] = None,
        blockSize : typing___Optional[typing___Text] = None,
        blockNumber : typing___Optional[int] = None,
        version : typing___Optional[int] = None,
        deployCount : typing___Optional[int] = None,
        tupleSpaceHash : typing___Optional[typing___Text] = None,
        timestamp : typing___Optional[int] = None,
        faultTolerance : typing___Optional[float] = None,
        mainParentHash : typing___Optional[typing___Text] = None,
        parentsHashList : typing___Optional[typing___Iterable[typing___Text]] = None,
        sender : typing___Optional[typing___Text] = None,
        shardId : typing___Optional[typing___Text] = None,
        bondsValidatorList : typing___Optional[typing___Iterable[typing___Text]] = None,
        deployCost : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",u"blockNumber",u"blockSize",u"bondsValidatorList",u"deployCost",u"deployCount",u"faultTolerance",u"mainParentHash",u"parentsHashList",u"sender",u"shardId",u"timestamp",u"tupleSpaceHash",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",b"blockHash",u"blockNumber",b"blockNumber",u"blockSize",b"blockSize",u"bondsValidatorList",b"bondsValidatorList",u"deployCost",b"deployCost",u"deployCount",b"deployCount",u"faultTolerance",b"faultTolerance",u"mainParentHash",b"mainParentHash",u"parentsHashList",b"parentsHashList",u"sender",b"sender",u"shardId",b"shardId",u"timestamp",b"timestamp",u"tupleSpaceHash",b"tupleSpaceHash",u"version",b"version"]) -> None: ...

class DataWithBlockInfo(google___protobuf___message___Message):

    @property
    def postBlockData(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RhoTypes_pb2___Par]: ...

    @property
    def block(self) -> LightBlockInfo: ...

    def __init__(self,
        *,
        postBlockData : typing___Optional[typing___Iterable[RhoTypes_pb2___Par]] = None,
        block : typing___Optional[LightBlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DataWithBlockInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"block"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"block",u"postBlockData"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"block",b"block"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"block",b"block",u"postBlockData",b"postBlockData"]) -> None: ...

class ContinuationsWithBlockInfo(google___protobuf___message___Message):

    @property
    def postBlockContinuations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[WaitingContinuationInfo]: ...

    @property
    def block(self) -> LightBlockInfo: ...

    def __init__(self,
        *,
        postBlockContinuations : typing___Optional[typing___Iterable[WaitingContinuationInfo]] = None,
        block : typing___Optional[LightBlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ContinuationsWithBlockInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"block"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"block",u"postBlockContinuations"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"block",b"block"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"block",b"block",u"postBlockContinuations",b"postBlockContinuations"]) -> None: ...

class WaitingContinuationInfo(google___protobuf___message___Message):

    @property
    def postBlockPatterns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RhoTypes_pb2___BindPattern]: ...

    @property
    def postBlockContinuation(self) -> RhoTypes_pb2___Par: ...

    def __init__(self,
        *,
        postBlockPatterns : typing___Optional[typing___Iterable[RhoTypes_pb2___BindPattern]] = None,
        postBlockContinuation : typing___Optional[RhoTypes_pb2___Par] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> WaitingContinuationInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"postBlockContinuation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"postBlockContinuation",u"postBlockPatterns"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"postBlockContinuation",b"postBlockContinuation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"postBlockContinuation",b"postBlockContinuation",u"postBlockPatterns",b"postBlockPatterns"]) -> None: ...

class DeployServiceResponseMeta(google___protobuf___message___Message):

    @property
    def DoDeploy(self) -> DeployServiceResponse: ...

    @property
    def getBlock(self) -> BlockQueryResponse: ...

    @property
    def visualizeDag(self) -> VisualizeBlocksResponse: ...

    @property
    def showMainChain(self) -> LightBlockInfo: ...

    @property
    def getBlocks(self) -> LightBlockInfo: ...

    @property
    def listenForDataAtName(self) -> ListeningNameDataResponse: ...

    @property
    def listenForContinuationAtName(self) -> ListeningNameContinuationResponse: ...

    @property
    def findDeploy(self) -> LightBlockQueryResponse: ...

    @property
    def previewPrivateNames(self) -> PrivateNamePreviewResponse: ...

    @property
    def lastFinalizedBlock(self) -> BlockQueryResponse: ...

    def __init__(self,
        *,
        DoDeploy : typing___Optional[DeployServiceResponse] = None,
        getBlock : typing___Optional[BlockQueryResponse] = None,
        visualizeDag : typing___Optional[VisualizeBlocksResponse] = None,
        showMainChain : typing___Optional[LightBlockInfo] = None,
        getBlocks : typing___Optional[LightBlockInfo] = None,
        listenForDataAtName : typing___Optional[ListeningNameDataResponse] = None,
        listenForContinuationAtName : typing___Optional[ListeningNameContinuationResponse] = None,
        findDeploy : typing___Optional[LightBlockQueryResponse] = None,
        previewPrivateNames : typing___Optional[PrivateNamePreviewResponse] = None,
        lastFinalizedBlock : typing___Optional[BlockQueryResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeployServiceResponseMeta: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"DoDeploy",u"findDeploy",u"getBlock",u"getBlocks",u"lastFinalizedBlock",u"listenForContinuationAtName",u"listenForDataAtName",u"previewPrivateNames",u"showMainChain",u"visualizeDag"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"DoDeploy",u"findDeploy",u"getBlock",u"getBlocks",u"lastFinalizedBlock",u"listenForContinuationAtName",u"listenForDataAtName",u"previewPrivateNames",u"showMainChain",u"visualizeDag"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"DoDeploy",b"DoDeploy",u"findDeploy",b"findDeploy",u"getBlock",b"getBlock",u"getBlocks",b"getBlocks",u"lastFinalizedBlock",b"lastFinalizedBlock",u"listenForContinuationAtName",b"listenForContinuationAtName",u"listenForDataAtName",b"listenForDataAtName",u"previewPrivateNames",b"previewPrivateNames",u"showMainChain",b"showMainChain",u"visualizeDag",b"visualizeDag"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"DoDeploy",b"DoDeploy",u"findDeploy",b"findDeploy",u"getBlock",b"getBlock",u"getBlocks",b"getBlocks",u"lastFinalizedBlock",b"lastFinalizedBlock",u"listenForContinuationAtName",b"listenForContinuationAtName",u"listenForDataAtName",b"listenForDataAtName",u"previewPrivateNames",b"previewPrivateNames",u"showMainChain",b"showMainChain",u"visualizeDag",b"visualizeDag"]) -> None: ...
