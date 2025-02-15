class Node {
    constructor (key, next=null, prev=null) {
        this.key = key;
        this.next = next;
        this.prev = prev;
    }
}

class LRU {
    constructor (capacity=5) {
        this.lookup = {}
        this.size = 0;
        this.capacity = capacity;
        this.head = new Node();
        this.tail = new Node();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    addItem (key) {
        if (this.lookup[key]) {
            const node = this.remove(this.lookup[key]);
            this.append(node);
        } else {
            const node = new Node(key);
            this.lookup[key] = node;
            this.append(node);
            this.size += 1;
        }

        while (this.size > this.capacity) {
            this.evict();
        }
    }

    append (node) {
        node.next = this.tail;
        node.prev = this.tail.prev;
        node.prev.next = node;
        this.tail.prev = node;
        return node;
    }

    remove (node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        return node;
    }
    
    evict () {
        if (!this.head.next.next) return;
        this.head.next = this.head.next.next;
        this.head.next.prev = this.head;
        this.size -= 1;
    }

    readCache () {
        const items = [];
        let n = this.head.next;
        while (n.next) {
            items.push(n.key);
            n = n.next;
        }
        return items;
    }
}

function processItems (strArr) {
    const lru = new LRU();
    for (let key of strArr) {
        lru.addItem(key);
    }
    return lru.readCache();
}

console.log(processItems(['A', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'E', 'E', 'A']));
