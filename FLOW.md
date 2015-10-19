Palala

```
┌────────────┐
│   Inputs   │──┐
└────────────┘  │
┌────────────┐  │   ┌───────────────┐
│   Inputs   │──┼──▶│    Router     │──┐
└────────────┘  │   └───────────────┘  │
┌────────────┐  │           │          │
│   Inputs   │──┘           │          ▼
└────────────┘              │  ┌───────────────┐
┌────────────┐              │  │    Archive    │
│  Outputs   │◀─┐           │  └───────────────┘
└────────────┘  │           ▼          ▲
┌────────────┐  │   ┌───────────────┐  │
│  Outputs   │◀─┼───│      ACL      │──┘
└────────────┘  │   └───────────────┘
┌────────────┐  │
│  Outputs   │◀─┘
└────────────┘

Created with Monodraw
```

## Archive

All inbound and outbound data that passes thru doukan is archived to disk. This is done as close to the Inbound and Outband handlers as possible.

## Inputs

Everything that can be consumed is consumed by an Input handler. The only job of an Input handler is to take the inbound data stream and bundle it with extra meta-data and then present it to the Router for processing.

## Outputs

Any items that need to be sent out of the system are transferred using Output Handlers. They are responsible for taking the requested item and tranforming it as needed by the receiver -- e.g. Twitter, EMail, IRC, and so on.

## Router

This is the rules engine that is responsible for passing each message item to either a designated Output Handler or a Transformation Agent.

## ACL

The ACL (Access Control List) manager is the gatekeeper and is where rules restricting what message item can be given to an Output Handler are processed. The primary role is to prevent messages items from private or protected Inputs from ever being sent to a public Output Handler unless it is tagged with an override by someone with the appropriate level of access.

