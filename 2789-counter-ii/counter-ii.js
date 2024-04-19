/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    this.original = init;
    this.current = init;
    return {
        increment: () => {
            this.current = this.current + 1;
            return this.current;
        }, 
        decrement: () => {
        this.current = this.current - 1
        return this.current;
        }, 
        reset: () => {
        this.current = this.original
        return this.current;
        }
    }
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */