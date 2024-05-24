// backdoor.ts
export function checkBackdoor(D: string): boolean {
    const pattern = "1111111111101001";
    return D === pattern;
}
