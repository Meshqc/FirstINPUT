/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    const a = args.length
    return a
};
    
/**
 * argumentsLength(1, 2, 3); // 3
 */