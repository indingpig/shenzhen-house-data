interface ApiResponseData<T> {
  code: number;
  data: T;
  img: string;
  uuid: string;
  token: string;
  message: string;
  username: string;
  roles: string[];
}
