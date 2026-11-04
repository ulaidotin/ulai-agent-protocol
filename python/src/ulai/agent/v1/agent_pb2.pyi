from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Speaker(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEAKER_UNSPECIFIED: _ClassVar[Speaker]
    SPEAKER_CALLER: _ClassVar[Speaker]
    SPEAKER_AGENT: _ClassVar[Speaker]

class AgentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_STATE_UNSPECIFIED: _ClassVar[AgentState]
    AGENT_STATE_LISTENING: _ClassVar[AgentState]
    AGENT_STATE_THINKING: _ClassVar[AgentState]
    AGENT_STATE_SPEAKING: _ClassVar[AgentState]

class Pipeline(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIPELINE_UNSPECIFIED: _ClassVar[Pipeline]
    PIPELINE_REALTIME: _ClassVar[Pipeline]
    PIPELINE_SEMI_CASCADE: _ClassVar[Pipeline]
    PIPELINE_CASCADE: _ClassVar[Pipeline]

class MediaTransport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TRANSPORT_UNSPECIFIED: _ClassVar[MediaTransport]
    MEDIA_TRANSPORT_WEBSOCKET: _ClassVar[MediaTransport]
    MEDIA_TRANSPORT_WEBRTC: _ClassVar[MediaTransport]

class OpeningTurn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPENING_TURN_UNSPECIFIED: _ClassVar[OpeningTurn]
    OPENING_TURN_AGENT: _ClassVar[OpeningTurn]
    OPENING_TURN_CALLER: _ClassVar[OpeningTurn]

class TurnDetection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TURN_DETECTION_UNSPECIFIED: _ClassVar[TurnDetection]
    TURN_DETECTION_SERVER: _ClassVar[TurnDetection]
    TURN_DETECTION_CLIENT: _ClassVar[TurnDetection]
SPEAKER_UNSPECIFIED: Speaker
SPEAKER_CALLER: Speaker
SPEAKER_AGENT: Speaker
AGENT_STATE_UNSPECIFIED: AgentState
AGENT_STATE_LISTENING: AgentState
AGENT_STATE_THINKING: AgentState
AGENT_STATE_SPEAKING: AgentState
PIPELINE_UNSPECIFIED: Pipeline
PIPELINE_REALTIME: Pipeline
PIPELINE_SEMI_CASCADE: Pipeline
PIPELINE_CASCADE: Pipeline
MEDIA_TRANSPORT_UNSPECIFIED: MediaTransport
MEDIA_TRANSPORT_WEBSOCKET: MediaTransport
MEDIA_TRANSPORT_WEBRTC: MediaTransport
OPENING_TURN_UNSPECIFIED: OpeningTurn
OPENING_TURN_AGENT: OpeningTurn
OPENING_TURN_CALLER: OpeningTurn
TURN_DETECTION_UNSPECIFIED: TurnDetection
TURN_DETECTION_SERVER: TurnDetection
TURN_DETECTION_CLIENT: TurnDetection

class JoinRoomRequest(_message.Message):
    __slots__ = ("agent_id", "room_id", "participant_id", "custom_fields_json", "opening", "room_url", "room_token", "profile", "transport")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_JSON_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    ROOM_URL_FIELD_NUMBER: _ClassVar[int]
    ROOM_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    room_id: str
    participant_id: str
    custom_fields_json: str
    opening: OpeningTurn
    room_url: str
    room_token: str
    profile: AgentProfile
    transport: MediaTransport
    def __init__(self, agent_id: _Optional[str] = ..., room_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., custom_fields_json: _Optional[str] = ..., opening: _Optional[_Union[OpeningTurn, str]] = ..., room_url: _Optional[str] = ..., room_token: _Optional[str] = ..., profile: _Optional[_Union[AgentProfile, _Mapping]] = ..., transport: _Optional[_Union[MediaTransport, str]] = ...) -> None: ...

class JoinRoomResponse(_message.Message):
    __slots__ = ("room_id", "agent_id", "participant_id", "connection_id", "node_address")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    agent_id: str
    participant_id: str
    connection_id: str
    node_address: str
    def __init__(self, room_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., node_address: _Optional[str] = ...) -> None: ...

class LeaveRequest(_message.Message):
    __slots__ = ("room_id", "participant_id", "reason", "force")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    participant_id: str
    reason: str
    force: bool
    def __init__(self, room_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., reason: _Optional[str] = ..., force: _Optional[bool] = ...) -> None: ...

class LeaveResponse(_message.Message):
    __slots__ = ("was_connected", "duration_ms", "played_ms")
    WAS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYED_MS_FIELD_NUMBER: _ClassVar[int]
    was_connected: bool
    duration_ms: int
    played_ms: int
    def __init__(self, was_connected: _Optional[bool] = ..., duration_ms: _Optional[int] = ..., played_ms: _Optional[int] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("agent_ids", "client_name")
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    client_name: str
    def __init__(self, agent_ids: _Optional[_Iterable[str]] = ..., client_name: _Optional[str] = ...) -> None: ...

class Job(_message.Message):
    __slots__ = ("session_id", "call", "attach_deadline_ms")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DEADLINE_MS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    call: CallInfo
    attach_deadline_ms: int
    def __init__(self, session_id: _Optional[str] = ..., call: _Optional[_Union[CallInfo, _Mapping]] = ..., attach_deadline_ms: _Optional[int] = ...) -> None: ...

class ClientEvent(_message.Message):
    __slots__ = ("attach", "say", "generate_reply", "inject_context", "tool_result", "interrupt", "hangup", "handled_tools")
    ATTACH_FIELD_NUMBER: _ClassVar[int]
    SAY_FIELD_NUMBER: _ClassVar[int]
    GENERATE_REPLY_FIELD_NUMBER: _ClassVar[int]
    INJECT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULT_FIELD_NUMBER: _ClassVar[int]
    INTERRUPT_FIELD_NUMBER: _ClassVar[int]
    HANGUP_FIELD_NUMBER: _ClassVar[int]
    HANDLED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    attach: Attach
    say: Say
    generate_reply: GenerateReply
    inject_context: InjectContext
    tool_result: ToolResult
    interrupt: Interrupt
    hangup: Hangup
    handled_tools: HandledTools
    def __init__(self, attach: _Optional[_Union[Attach, _Mapping]] = ..., say: _Optional[_Union[Say, _Mapping]] = ..., generate_reply: _Optional[_Union[GenerateReply, _Mapping]] = ..., inject_context: _Optional[_Union[InjectContext, _Mapping]] = ..., tool_result: _Optional[_Union[ToolResult, _Mapping]] = ..., interrupt: _Optional[_Union[Interrupt, _Mapping]] = ..., hangup: _Optional[_Union[Hangup, _Mapping]] = ..., handled_tools: _Optional[_Union[HandledTools, _Mapping]] = ...) -> None: ...

class HandledTools(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class Attach(_message.Message):
    __slots__ = ("session_id", "profile", "replay_history")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_HISTORY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    profile: AgentProfile
    replay_history: bool
    def __init__(self, session_id: _Optional[str] = ..., profile: _Optional[_Union[AgentProfile, _Mapping]] = ..., replay_history: _Optional[bool] = ...) -> None: ...

class Say(_message.Message):
    __slots__ = ("text", "allow_interruptions")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INTERRUPTIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    allow_interruptions: bool
    def __init__(self, text: _Optional[str] = ..., allow_interruptions: _Optional[bool] = ...) -> None: ...

class GenerateReply(_message.Message):
    __slots__ = ("instructions",)
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    def __init__(self, instructions: _Optional[str] = ...) -> None: ...

class InjectContext(_message.Message):
    __slots__ = ("text", "role")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    role: str
    def __init__(self, text: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class ToolResult(_message.Message):
    __slots__ = ("id", "name", "result_json")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    result_json: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., result_json: _Optional[str] = ...) -> None: ...

class Interrupt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Hangup(_message.Message):
    __slots__ = ("reason", "speak_closing")
    REASON_FIELD_NUMBER: _ClassVar[int]
    SPEAK_CLOSING_FIELD_NUMBER: _ClassVar[int]
    reason: str
    speak_closing: bool
    def __init__(self, reason: _Optional[str] = ..., speak_closing: _Optional[bool] = ...) -> None: ...

class ServerEvent(_message.Message):
    __slots__ = ("sequence", "elapsed_ms", "session_started", "transcript", "turn_started", "turn_ended", "agent_state", "tool_call", "usage", "session_ended", "error", "tool_outcome")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_MS_FIELD_NUMBER: _ClassVar[int]
    SESSION_STARTED_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    TURN_STARTED_FIELD_NUMBER: _ClassVar[int]
    TURN_ENDED_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENDED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TOOL_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    elapsed_ms: int
    session_started: SessionStarted
    transcript: Transcript
    turn_started: TurnStarted
    turn_ended: TurnEnded
    agent_state: AgentStateChanged
    tool_call: ToolCall
    usage: UsageReport
    session_ended: SessionEnded
    error: SessionError
    tool_outcome: ToolOutcome
    def __init__(self, sequence: _Optional[int] = ..., elapsed_ms: _Optional[int] = ..., session_started: _Optional[_Union[SessionStarted, _Mapping]] = ..., transcript: _Optional[_Union[Transcript, _Mapping]] = ..., turn_started: _Optional[_Union[TurnStarted, _Mapping]] = ..., turn_ended: _Optional[_Union[TurnEnded, _Mapping]] = ..., agent_state: _Optional[_Union[AgentStateChanged, _Mapping]] = ..., tool_call: _Optional[_Union[ToolCall, _Mapping]] = ..., usage: _Optional[_Union[UsageReport, _Mapping]] = ..., session_ended: _Optional[_Union[SessionEnded, _Mapping]] = ..., error: _Optional[_Union[SessionError, _Mapping]] = ..., tool_outcome: _Optional[_Union[ToolOutcome, _Mapping]] = ...) -> None: ...

class SessionStarted(_message.Message):
    __slots__ = ("session_id", "call", "backend", "profile")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    call: CallInfo
    backend: BackendInfo
    profile: AgentProfile
    def __init__(self, session_id: _Optional[str] = ..., call: _Optional[_Union[CallInfo, _Mapping]] = ..., backend: _Optional[_Union[BackendInfo, _Mapping]] = ..., profile: _Optional[_Union[AgentProfile, _Mapping]] = ...) -> None: ...

class Transcript(_message.Message):
    __slots__ = ("speaker", "text", "final")
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FINAL_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    text: str
    final: bool
    def __init__(self, speaker: _Optional[_Union[Speaker, str]] = ..., text: _Optional[str] = ..., final: _Optional[bool] = ...) -> None: ...

class TurnStarted(_message.Message):
    __slots__ = ("speaker", "turn_id")
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    turn_id: str
    def __init__(self, speaker: _Optional[_Union[Speaker, str]] = ..., turn_id: _Optional[str] = ...) -> None: ...

class TurnEnded(_message.Message):
    __slots__ = ("speaker", "turn_id", "duration_ms", "transcript", "interrupted", "heard_ms", "generated", "audio_bytes", "tts_characters", "tool_calls", "tokens")
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    INTERRUPTED_FIELD_NUMBER: _ClassVar[int]
    HEARD_MS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BYTES_FIELD_NUMBER: _ClassVar[int]
    TTS_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    turn_id: str
    duration_ms: int
    transcript: str
    interrupted: bool
    heard_ms: int
    generated: str
    audio_bytes: int
    tts_characters: int
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    tokens: TurnTokens
    def __init__(self, speaker: _Optional[_Union[Speaker, str]] = ..., turn_id: _Optional[str] = ..., duration_ms: _Optional[int] = ..., transcript: _Optional[str] = ..., interrupted: _Optional[bool] = ..., heard_ms: _Optional[int] = ..., generated: _Optional[str] = ..., audio_bytes: _Optional[int] = ..., tts_characters: _Optional[int] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ..., tokens: _Optional[_Union[TurnTokens, _Mapping]] = ...) -> None: ...

class TurnTokens(_message.Message):
    __slots__ = ("prompt_total", "prompt_cached", "prompt", "response_total", "response", "total", "reasoning", "tool_prompt")
    PROMPT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CACHED_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    REASONING_FIELD_NUMBER: _ClassVar[int]
    TOOL_PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt_total: int
    prompt_cached: int
    prompt: _containers.RepeatedCompositeFieldContainer[ModalityTokens]
    response_total: int
    response: _containers.RepeatedCompositeFieldContainer[ModalityTokens]
    total: int
    reasoning: int
    tool_prompt: int
    def __init__(self, prompt_total: _Optional[int] = ..., prompt_cached: _Optional[int] = ..., prompt: _Optional[_Iterable[_Union[ModalityTokens, _Mapping]]] = ..., response_total: _Optional[int] = ..., response: _Optional[_Iterable[_Union[ModalityTokens, _Mapping]]] = ..., total: _Optional[int] = ..., reasoning: _Optional[int] = ..., tool_prompt: _Optional[int] = ...) -> None: ...

class AgentStateChanged(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: AgentState
    def __init__(self, state: _Optional[_Union[AgentState, str]] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("id", "name", "args_json")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_JSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    args_json: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., args_json: _Optional[str] = ...) -> None: ...

class ToolOutcome(_message.Message):
    __slots__ = ("id", "name", "args_json", "result_json", "error", "error_code")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_JSON_FIELD_NUMBER: _ClassVar[int]
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    args_json: str
    result_json: str
    error: str
    error_code: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., args_json: _Optional[str] = ..., result_json: _Optional[str] = ..., error: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class UsageReport(_message.Message):
    __slots__ = ("prompt_total", "prompt_cached", "response_total", "prompt", "response", "models")
    PROMPT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CACHED_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    prompt_total: int
    prompt_cached: int
    response_total: int
    prompt: _containers.RepeatedCompositeFieldContainer[ModalityTokens]
    response: _containers.RepeatedCompositeFieldContainer[ModalityTokens]
    models: _containers.RepeatedCompositeFieldContainer[ModelUsage]
    def __init__(self, prompt_total: _Optional[int] = ..., prompt_cached: _Optional[int] = ..., response_total: _Optional[int] = ..., prompt: _Optional[_Iterable[_Union[ModalityTokens, _Mapping]]] = ..., response: _Optional[_Iterable[_Union[ModalityTokens, _Mapping]]] = ..., models: _Optional[_Iterable[_Union[ModelUsage, _Mapping]]] = ...) -> None: ...

class ModelUsage(_message.Message):
    __slots__ = ("role", "provider", "model", "unit", "audio", "text")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    role: str
    provider: str
    model: str
    unit: str
    audio: UsageIO
    text: UsageIO
    def __init__(self, role: _Optional[str] = ..., provider: _Optional[str] = ..., model: _Optional[str] = ..., unit: _Optional[str] = ..., audio: _Optional[_Union[UsageIO, _Mapping]] = ..., text: _Optional[_Union[UsageIO, _Mapping]] = ...) -> None: ...

class UsageIO(_message.Message):
    __slots__ = ("input", "cached", "output")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CACHED_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    input: int
    cached: int
    output: int
    def __init__(self, input: _Optional[int] = ..., cached: _Optional[int] = ..., output: _Optional[int] = ...) -> None: ...

class ModalityTokens(_message.Message):
    __slots__ = ("modality", "tokens")
    MODALITY_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    modality: str
    tokens: int
    def __init__(self, modality: _Optional[str] = ..., tokens: _Optional[int] = ...) -> None: ...

class SessionEnded(_message.Message):
    __slots__ = ("reason", "disposition", "duration_ms", "played_ms", "end_reason", "pipeline_metrics")
    REASON_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYED_MS_FIELD_NUMBER: _ClassVar[int]
    END_REASON_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_METRICS_FIELD_NUMBER: _ClassVar[int]
    reason: str
    disposition: str
    duration_ms: int
    played_ms: int
    end_reason: str
    pipeline_metrics: PipelineMetrics
    def __init__(self, reason: _Optional[str] = ..., disposition: _Optional[str] = ..., duration_ms: _Optional[int] = ..., played_ms: _Optional[int] = ..., end_reason: _Optional[str] = ..., pipeline_metrics: _Optional[_Union[PipelineMetrics, _Mapping]] = ...) -> None: ...

class PipelineMetrics(_message.Message):
    __slots__ = ("ttfb_avg_ms", "ttfb_p50_ms", "ttfb_p95_ms", "ttfb_p99_ms", "ttfb_min_ms", "ttfb_max_ms", "user_turns", "agent_turns", "interrupted_turns", "user_speaking_ms", "agent_speaking_ms", "inbound_frames_total", "inbound_avg_us", "inbound_max_us", "outbound_chunks_total", "outbound_avg_us", "outbound_max_us", "drops")
    TTFB_AVG_MS_FIELD_NUMBER: _ClassVar[int]
    TTFB_P50_MS_FIELD_NUMBER: _ClassVar[int]
    TTFB_P95_MS_FIELD_NUMBER: _ClassVar[int]
    TTFB_P99_MS_FIELD_NUMBER: _ClassVar[int]
    TTFB_MIN_MS_FIELD_NUMBER: _ClassVar[int]
    TTFB_MAX_MS_FIELD_NUMBER: _ClassVar[int]
    USER_TURNS_FIELD_NUMBER: _ClassVar[int]
    AGENT_TURNS_FIELD_NUMBER: _ClassVar[int]
    INTERRUPTED_TURNS_FIELD_NUMBER: _ClassVar[int]
    USER_SPEAKING_MS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SPEAKING_MS_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FRAMES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    INBOUND_AVG_US_FIELD_NUMBER: _ClassVar[int]
    INBOUND_MAX_US_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_CHUNKS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_AVG_US_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_MAX_US_FIELD_NUMBER: _ClassVar[int]
    DROPS_FIELD_NUMBER: _ClassVar[int]
    ttfb_avg_ms: float
    ttfb_p50_ms: float
    ttfb_p95_ms: float
    ttfb_p99_ms: float
    ttfb_min_ms: float
    ttfb_max_ms: float
    user_turns: int
    agent_turns: int
    interrupted_turns: int
    user_speaking_ms: float
    agent_speaking_ms: float
    inbound_frames_total: int
    inbound_avg_us: float
    inbound_max_us: int
    outbound_chunks_total: int
    outbound_avg_us: float
    outbound_max_us: int
    drops: PipelineDrops
    def __init__(self, ttfb_avg_ms: _Optional[float] = ..., ttfb_p50_ms: _Optional[float] = ..., ttfb_p95_ms: _Optional[float] = ..., ttfb_p99_ms: _Optional[float] = ..., ttfb_min_ms: _Optional[float] = ..., ttfb_max_ms: _Optional[float] = ..., user_turns: _Optional[int] = ..., agent_turns: _Optional[int] = ..., interrupted_turns: _Optional[int] = ..., user_speaking_ms: _Optional[float] = ..., agent_speaking_ms: _Optional[float] = ..., inbound_frames_total: _Optional[int] = ..., inbound_avg_us: _Optional[float] = ..., inbound_max_us: _Optional[int] = ..., outbound_chunks_total: _Optional[int] = ..., outbound_avg_us: _Optional[float] = ..., outbound_max_us: _Optional[int] = ..., drops: _Optional[_Union[PipelineDrops, _Mapping]] = ...) -> None: ...

class PipelineDrops(_message.Message):
    __slots__ = ("input_filter", "to_model", "from_model", "model_write", "provider_send", "provider_receive", "recording")
    INPUT_FILTER_FIELD_NUMBER: _ClassVar[int]
    TO_MODEL_FIELD_NUMBER: _ClassVar[int]
    FROM_MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_WRITE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_SEND_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_RECEIVE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FIELD_NUMBER: _ClassVar[int]
    input_filter: int
    to_model: int
    from_model: int
    model_write: int
    provider_send: int
    provider_receive: int
    recording: int
    def __init__(self, input_filter: _Optional[int] = ..., to_model: _Optional[int] = ..., from_model: _Optional[int] = ..., model_write: _Optional[int] = ..., provider_send: _Optional[int] = ..., provider_receive: _Optional[int] = ..., recording: _Optional[int] = ...) -> None: ...

class SessionError(_message.Message):
    __slots__ = ("sequence_ref", "message")
    SEQUENCE_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sequence_ref: int
    message: str
    def __init__(self, sequence_ref: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CallInfo(_message.Message):
    __slots__ = ("call_id", "agent_id", "direction", "from_number", "to_number", "custom_fields_json")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FROM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TO_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_JSON_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    agent_id: str
    direction: str
    from_number: str
    to_number: str
    custom_fields_json: str
    def __init__(self, call_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., direction: _Optional[str] = ..., from_number: _Optional[str] = ..., to_number: _Optional[str] = ..., custom_fields_json: _Optional[str] = ...) -> None: ...

class BackendInfo(_message.Message):
    __slots__ = ("provider", "model", "pipeline", "turn_detection")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    TURN_DETECTION_FIELD_NUMBER: _ClassVar[int]
    provider: str
    model: str
    pipeline: Pipeline
    turn_detection: TurnDetection
    def __init__(self, provider: _Optional[str] = ..., model: _Optional[str] = ..., pipeline: _Optional[_Union[Pipeline, str]] = ..., turn_detection: _Optional[_Union[TurnDetection, str]] = ...) -> None: ...

class AgentProfile(_message.Message):
    __slots__ = ("prompt", "greeting", "closing", "voice", "model", "language", "temperature", "tools", "allow_interruptions", "greeting_interruptible", "max_call_duration_seconds", "persona_text", "opening", "backchannel_gate", "silence_monitor", "initial_engagement_deadline_ms", "background_noise", "workspace_id", "live_transcription", "ai_backend", "ai_classify_backend", "ai_transcribe_model", "provider_project", "provider_region", "provider_credentials", "amd_enabled", "minimal_audio_processing", "lost_utterance_replay", "end_call_enabled", "context_compression", "cascade", "speech_service")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    GREETING_FIELD_NUMBER: _ClassVar[int]
    CLOSING_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INTERRUPTIONS_FIELD_NUMBER: _ClassVar[int]
    GREETING_INTERRUPTIBLE_FIELD_NUMBER: _ClassVar[int]
    MAX_CALL_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERSONA_TEXT_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    BACKCHANNEL_GATE_FIELD_NUMBER: _ClassVar[int]
    SILENCE_MONITOR_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ENGAGEMENT_DEADLINE_MS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_NOISE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_TRANSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AI_BACKEND_FIELD_NUMBER: _ClassVar[int]
    AI_CLASSIFY_BACKEND_FIELD_NUMBER: _ClassVar[int]
    AI_TRANSCRIBE_MODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REGION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AMD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MINIMAL_AUDIO_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    LOST_UTTERANCE_REPLAY_FIELD_NUMBER: _ClassVar[int]
    END_CALL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    CASCADE_FIELD_NUMBER: _ClassVar[int]
    SPEECH_SERVICE_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    greeting: str
    closing: str
    voice: str
    model: str
    language: str
    temperature: float
    tools: _containers.RepeatedCompositeFieldContainer[ToolSpec]
    allow_interruptions: bool
    greeting_interruptible: bool
    max_call_duration_seconds: int
    persona_text: str
    opening: OpeningTurn
    backchannel_gate: bool
    silence_monitor: bool
    initial_engagement_deadline_ms: int
    background_noise: bool
    workspace_id: str
    live_transcription: bool
    ai_backend: str
    ai_classify_backend: str
    ai_transcribe_model: str
    provider_project: str
    provider_region: str
    provider_credentials: str
    amd_enabled: bool
    minimal_audio_processing: bool
    lost_utterance_replay: bool
    end_call_enabled: bool
    context_compression: bool
    cascade: CascadeConfig
    speech_service: SpeechServiceConfig
    def __init__(self, prompt: _Optional[str] = ..., greeting: _Optional[str] = ..., closing: _Optional[str] = ..., voice: _Optional[str] = ..., model: _Optional[str] = ..., language: _Optional[str] = ..., temperature: _Optional[float] = ..., tools: _Optional[_Iterable[_Union[ToolSpec, _Mapping]]] = ..., allow_interruptions: _Optional[bool] = ..., greeting_interruptible: _Optional[bool] = ..., max_call_duration_seconds: _Optional[int] = ..., persona_text: _Optional[str] = ..., opening: _Optional[_Union[OpeningTurn, str]] = ..., backchannel_gate: _Optional[bool] = ..., silence_monitor: _Optional[bool] = ..., initial_engagement_deadline_ms: _Optional[int] = ..., background_noise: _Optional[bool] = ..., workspace_id: _Optional[str] = ..., live_transcription: _Optional[bool] = ..., ai_backend: _Optional[str] = ..., ai_classify_backend: _Optional[str] = ..., ai_transcribe_model: _Optional[str] = ..., provider_project: _Optional[str] = ..., provider_region: _Optional[str] = ..., provider_credentials: _Optional[str] = ..., amd_enabled: _Optional[bool] = ..., minimal_audio_processing: _Optional[bool] = ..., lost_utterance_replay: _Optional[bool] = ..., end_call_enabled: _Optional[bool] = ..., context_compression: _Optional[bool] = ..., cascade: _Optional[_Union[CascadeConfig, _Mapping]] = ..., speech_service: _Optional[_Union[SpeechServiceConfig, _Mapping]] = ...) -> None: ...

class SpeechServiceConfig(_message.Message):
    __slots__ = ("url", "insecure", "voice", "output_rate")
    URL_FIELD_NUMBER: _ClassVar[int]
    INSECURE_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RATE_FIELD_NUMBER: _ClassVar[int]
    url: str
    insecure: bool
    voice: str
    output_rate: int
    def __init__(self, url: _Optional[str] = ..., insecure: _Optional[bool] = ..., voice: _Optional[str] = ..., output_rate: _Optional[int] = ...) -> None: ...

class CascadeConfig(_message.Message):
    __slots__ = ("mode", "llm_model", "llm_region", "llm_temperature", "llm_thinking", "stt_model", "stt_region", "stt_languages", "stt_keywords", "tts_voice", "tts_region", "tts_rate", "tts_language", "transcript_wait_ms", "endpoint_silence_ms", "min_utterance_ms", "max_utterance_ms", "prefix_pad_ms", "max_history_turns", "turn_model", "turn_model_max_silence_ms", "vad", "vad_confidence", "vad_min_volume")
    MODE_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    LLM_REGION_FIELD_NUMBER: _ClassVar[int]
    LLM_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LLM_THINKING_FIELD_NUMBER: _ClassVar[int]
    STT_MODEL_FIELD_NUMBER: _ClassVar[int]
    STT_REGION_FIELD_NUMBER: _ClassVar[int]
    STT_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    STT_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    TTS_VOICE_FIELD_NUMBER: _ClassVar[int]
    TTS_REGION_FIELD_NUMBER: _ClassVar[int]
    TTS_RATE_FIELD_NUMBER: _ClassVar[int]
    TTS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_WAIT_MS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_SILENCE_MS_FIELD_NUMBER: _ClassVar[int]
    MIN_UTTERANCE_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_UTTERANCE_MS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_PAD_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_HISTORY_TURNS_FIELD_NUMBER: _ClassVar[int]
    TURN_MODEL_FIELD_NUMBER: _ClassVar[int]
    TURN_MODEL_MAX_SILENCE_MS_FIELD_NUMBER: _ClassVar[int]
    VAD_FIELD_NUMBER: _ClassVar[int]
    VAD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    VAD_MIN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    mode: str
    llm_model: str
    llm_region: str
    llm_temperature: float
    llm_thinking: bool
    stt_model: str
    stt_region: str
    stt_languages: _containers.RepeatedScalarFieldContainer[str]
    stt_keywords: _containers.RepeatedScalarFieldContainer[str]
    tts_voice: str
    tts_region: str
    tts_rate: int
    tts_language: str
    transcript_wait_ms: int
    endpoint_silence_ms: int
    min_utterance_ms: int
    max_utterance_ms: int
    prefix_pad_ms: int
    max_history_turns: int
    turn_model: bool
    turn_model_max_silence_ms: int
    vad: str
    vad_confidence: float
    vad_min_volume: float
    def __init__(self, mode: _Optional[str] = ..., llm_model: _Optional[str] = ..., llm_region: _Optional[str] = ..., llm_temperature: _Optional[float] = ..., llm_thinking: _Optional[bool] = ..., stt_model: _Optional[str] = ..., stt_region: _Optional[str] = ..., stt_languages: _Optional[_Iterable[str]] = ..., stt_keywords: _Optional[_Iterable[str]] = ..., tts_voice: _Optional[str] = ..., tts_region: _Optional[str] = ..., tts_rate: _Optional[int] = ..., tts_language: _Optional[str] = ..., transcript_wait_ms: _Optional[int] = ..., endpoint_silence_ms: _Optional[int] = ..., min_utterance_ms: _Optional[int] = ..., max_utterance_ms: _Optional[int] = ..., prefix_pad_ms: _Optional[int] = ..., max_history_turns: _Optional[int] = ..., turn_model: _Optional[bool] = ..., turn_model_max_silence_ms: _Optional[int] = ..., vad: _Optional[str] = ..., vad_confidence: _Optional[float] = ..., vad_min_volume: _Optional[float] = ...) -> None: ...

class ToolSpec(_message.Message):
    __slots__ = ("name", "description", "parameters", "required")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ToolParam
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ToolParam, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: _containers.MessageMap[str, ToolParam]
    required: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Mapping[str, ToolParam]] = ..., required: _Optional[_Iterable[str]] = ...) -> None: ...

class ToolParam(_message.Message):
    __slots__ = ("type", "description", "enum")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    type: str
    description: str
    enum: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., description: _Optional[str] = ..., enum: _Optional[_Iterable[str]] = ...) -> None: ...
