class LoginLimiter {
    constructor(maxAttempts = 3) {
        this.maxAttempts = maxAttempts;
        this.failedAttempts = 0;
    }

    registerFailure() {
        this.failedAttempts += 1;

        if (this.failedAttempts > this.maxAttempts) {
            throw new Error("Account temporaneamente bloccato.");
        }

        return this.failedAttempts;
    }

    reset() {
        this.failedAttempts = 0;
    }
}

module.exports = LoginLimiter;