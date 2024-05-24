// encryption.ts
export function encrypt(D: string, K: string): string {
    let E = [];
    for (let i = 0; i < 16; i++) {
        if (i === 0 || i === 6 || i === 13) {
            E[i] = K[i] === '1' ? '0' : '1'; // NOT operation
        } else {
            E[i] = D[i] === K[i] ? '0' : '1'; // XOR operation
        }
    }
    return E.join('');
}
