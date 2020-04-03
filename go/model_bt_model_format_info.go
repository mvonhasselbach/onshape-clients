/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtModelFormatInfo struct for BtModelFormatInfo
type BtModelFormatInfo struct {
	CouldBeAssembly bool `json:"couldBeAssembly,omitempty"`
	Name string `json:"name,omitempty"`
	TranslatorName string `json:"translatorName,omitempty"`
}