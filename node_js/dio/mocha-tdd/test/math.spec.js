const Math = require('../src/math.js')
const expect = require('chai').expect
const sinon = require('sinon')

let value = 0

describe('Math class', function() {
    //hooks
    beforeEach(function() {
        // runs before each test in this block
        // before, beforeEach, afterEach, after
        value = 0
    })

    it/*.only*/('Sum two numbers', function(done) {
        const math = new Math()
        this.timeout(3000) //define o timeout do teste

        value = 5

        math.sum(value, 5, value => {
            expect(value).to.equal(10)
            done()
        })
    })

    it/*.skip*/('Multiply two numbers', function () {
        const math = new Math()

        value = 4

        expect(math.multiply(value, 5)).to.equal(20)
    })

    it('Calls req with sum and index values', function () {
        const req = {}
        const res = {
            load: sinon.spy()
        }
        const math = new Math()

        math.printSum(req, res, 5, 5)

        expect(res.load.calledOnce).to.be.true
    })
})