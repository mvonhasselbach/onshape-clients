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
// BtmParameterConfigured2222AllOf struct for BtmParameterConfigured2222AllOf
type BtmParameterConfigured2222AllOf struct {
	ValuesFieldIndex int32 `json:"valuesFieldIndex,omitempty"`
	ConfigurationParameterIdFieldIndex int32 `json:"configurationParameterIdFieldIndex,omitempty"`
	ConfigurationParameterId string `json:"configurationParameterId,omitempty"`
	Values []BtmConfiguredValue1341 `json:"values,omitempty"`
	BtType string `json:"btType,omitempty"`
}