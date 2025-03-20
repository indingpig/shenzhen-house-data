import 'pinia';

declare module 'pinia' {
  export interface PiniaCustomProperties<S> {
    hello: Ref<string>;
    $state: S & {
      hello: Ref<string>; // 这里定义你的自定义属性
    };
    $message: ({ message, type }: { message: string; type: 'success' | 'warning' | 'info' | 'error' }) => void;
  }
}
