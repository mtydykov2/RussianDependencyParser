/* DO NOT EDIT THIS FILE - it is machine generated */
#ifndef _Included_ru_aot_morph_JavaMorphAPI
#define _Included_ru_aot_morph_JavaMorphAPI

#include <jni_md.h>
#include <jni.h>
/* Header for class ru_aot_morph_JavaMorphAPI */

#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     ru_aot_morph_JavaMorphAPI
 * Method:    lookupWordImpl
 * Signature: (I[B)Lru/aot/morph/JavaMorphAPI/WordResult;
 */
JNIEXPORT jobject JNICALL Java_ru_aot_morph_JavaMorphAPI_lookupWordImpl
  (JNIEnv *, jclass, jint, jbyteArray);

/*
 * Class:     ru_aot_morph_JavaMorphAPI
 * Method:    initImpl
 * Signature: (I)V
 */
JNIEXPORT void JNICALL Java_ru_aot_morph_JavaMorphAPI_initImpl
  (JNIEnv *, jclass, jint);

/*
 * Class:     ru_aot_morph_JavaMorphAPI
 * Method:    closeImpl
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_ru_aot_morph_JavaMorphAPI_closeImpl
  (JNIEnv *, jclass);

#ifdef __cplusplus
}
#endif
#endif
