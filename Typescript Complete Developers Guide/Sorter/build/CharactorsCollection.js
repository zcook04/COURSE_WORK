"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CharactorsCollection = void 0;
var CharactorsCollection = /** @class */ (function () {
    function CharactorsCollection(data) {
        this.data = data;
    }
    Object.defineProperty(CharactorsCollection.prototype, "length", {
        get: function () {
            return this.data.length;
        },
        enumerable: false,
        configurable: true
    });
    CharactorsCollection.prototype.compare = function (leftIndex, rightIndex) {
        return (this.data[leftIndex].toLowerCase() > this.data[rightIndex].toLowerCase());
    };
    CharactorsCollection.prototype.swap = function (leftIndex, rightIndex) {
        var characters = this.data.split('');
        var leftHand = characters[leftIndex];
        characters[leftIndex] = characters[rightIndex];
        characters[rightIndex] = leftHand;
        this.data = characters.join('');
    };
    return CharactorsCollection;
}());
exports.CharactorsCollection = CharactorsCollection;
