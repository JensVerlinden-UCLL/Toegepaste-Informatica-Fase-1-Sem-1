export class CustomError extends Error {
  constructor(
    readonly status: number,
    message: string
  ) {
    super(message);
  }
}