/* Philip T.L.C. Clausen Jan 2017 plan@dtu.dk */

/*
 * Copyright (c) 2017, Philip Clausen, Technical University of Denmark
 * All rights reserved.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *		http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

#include "hashmapstr.h"
#include "hashmapstrindex.h"
#include "pherror.h"

int HashMapStrindex_add(HashMapStr *src, unsigned char *str) {
	
	unsigned hash, pos;
	BucketStr *node;
	
	hash = djb2(str);
	pos = hash & src->size;
	
	/* search hashmap */
	for(node = src->table[pos]; node; node = node->next) {
		if(hash == node->hash && strcmp((char *) str, (char *) node->str) == 0) {
			return node->num;
		}
	}
	
	if(++src->n == src->size) {
		HashMapStr_grow(src);
	}
	node = smalloc(sizeof(BucketStr));
	node->str = ustrdup(str);
	node->hash = hash;
	node->num = src->n - 1;
	node->uList = 0;
	node->next = src->table[pos];
	src->table[pos] = node;
	
	return -1;
}
