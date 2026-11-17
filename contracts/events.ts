export type EventEnvelope<TType extends string, TPayload> = {
  event_id: string;
  type: TType;
  occurred_at: string;
  payload: TPayload;
};

export type AGVPositionUpdated = EventEnvelope<"agv.position_updated", {
  agv_id: string;
  x: number;
  y: number;
  heading?: number;
}>;

export type TaskStatusChanged = EventEnvelope<"task.status_changed", {
  task_id: string;
  status: "pending" | "assigned" | "in_progress" | "completed" | "failed";
}>;

export type TwinEvent = AGVPositionUpdated | TaskStatusChanged;
