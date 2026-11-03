# ulai-agent-protocol

Generated protobuf and gRPC code for the Ulai agent API, package `ulai.agent.v1`.

**Everything under `go/ulai`, `python/src/ulai` and `js/ulai` is generated. Do not edit it by hand.**

## Services

| Service | RPC | Shape |
|---|---|---|
| `Session` | `Run` | bidirectional stream: `ClientEvent` ⇄ `ServerEvent` |
| `Dispatch` | `Subscribe` | server stream of `Job` |
| `Room` | `Join`, `Leave` | unary |

## Go

```sh
go get github.com/ulaidotin/ulai-agent-protocol
```

```go
import agentv1 "github.com/ulaidotin/ulai-agent-protocol/go/ulai/agent/v1"

client := agentv1.NewSessionClient(conn)
```

## Python (3.10+)

```sh
pip install "git+https://github.com/ulaidotin/ulai-agent-protocol.git#subdirectory=python"
```

```python
from ulai.agent.v1 import agent_pb2, agent_pb2_grpc

stub = agent_pb2_grpc.SessionStub(channel)
```

## JavaScript / TypeScript

Built with [protobuf-es](https://github.com/bufbuild/protobuf-es) v2 (`.js` plus `.d.ts`). Use the service descriptors with
[Connect](https://connectrpc.com/docs/node/using-clients) (`@connectrpc/connect` and `@connectrpc/connect-node`'s gRPC transport):

```ts
import { createClient } from "@connectrpc/connect";
import { createGrpcTransport } from "@connectrpc/connect-node";
import { Session } from "ulai-agent-protocol/ulai/agent/v1";

const client = createClient(Session, createGrpcTransport({ baseUrl: "https://host:port" }));
```
